"""
Created by SungMin Yoon on 2022-05-24..
Copyright (c) 2022 year NCC (National Cancer Center). All rights reserved.
"""
import vtk
from APP.config import vtkConstants
from vtkmodules.vtkCommonCore import vtkDataArray
import numpy


def numpy_to_vtk_use(data, multi_component=False, type='float'):
    '''
    multi_components: rgb has 3 components
    type：float or char
    '''

    if type == 'float':
        data_type = vtk.VTK_FLOAT
    elif type == 'char':
        data_type = vtk.VTK_UNSIGNED_CHAR
    else:
        raise RuntimeError('unknown type')

    if not multi_component:
        if len(data.shape) == 2:
            data = data[:, :, numpy.newaxis]

        flat_data_array = data.transpose(2, 1, 0).flatten()
        vtk_data = numpy_to_vtk(num_array=flat_data_array, deep=True, array_type=data_type)
        shape = data.shape

    else:
        assert len(data.shape) == 3, 'only test for 2D RGB'
        flat_data_array = data.transpose(0, 1, 2)
        flat_data_array = numpy.reshape(flat_data_array, newshape=[-1, data.shape[2]])

        vtk_data = numpy_to_vtk(num_array=flat_data_array, deep=True, array_type=data_type)
        shape = [data.shape[0], data.shape[1], 1]

    img = vtk.vtkImageData()
    img.GetPointData().SetScalars(vtk_data)
    img.SetDimensions(shape[0], shape[1], shape[2])

    return img


def create_vtk_array(vtk_arr_type):
    """Internal function used to make a VTK data array from another
    VTK array given the VTK array type.
    """
    return vtkDataArray.CreateDataArray(vtk_arr_type)


def get_numpy_array_type(vtk_array_type):
    """Returns a numpy array typecode given a VTK array type."""
    return get_vtk_to_numpy_typemap()[vtk_array_type]


def numpy_to_vtk(num_array, deep=0, array_type=None):
    """Converts a real numpy Array to a VTK array object.
    This function only works for real arrays.
    Complex arrays are NOT handled.  It also works for multi-component
    arrays.  However, only 1, and 2 dimensional arrays are supported.
    This function is very efficient, so large arrays should not be a
    problem.
    If the second argument is set to 1, the array is deep-copied from
    from numpy. This is not as efficient as the default behavior
    (shallow copy) and uses more memory but detaches the two arrays
    such that the numpy array can be released.
    WARNING: You must maintain a reference to the passed numpy array, if
    the numpy data is gc'd and VTK will point to garbage which will in
    the best case give you a segfault.
    Parameters:
    num_array
      a 1D or 2D, real numpy array.
    """

    z = numpy.asarray(num_array)
    if not z.flags.contiguous:
        z = numpy.ascontiguousarray(z)

    shape = z.shape
    assert z.flags.contiguous, 'Only contiguous arrays are supported.'
    assert len(shape) < 3, \
           "Only arrays of dimensionality 2 or lower are allowed!"
    assert not numpy.issubdtype(z.dtype, numpy.dtype(complex).type), \
           "Complex numpy arrays cannot be converted to vtk arrays."\
           "Use real() or imag() to get a component of the array before"\
           " passing it to vtk."

    # First make an array of the right type by using the typecode.
    if array_type:
        vtk_typecode = array_type
    else:
        vtk_typecode = get_vtk_array_type(z.dtype)
    result_array = create_vtk_array(vtk_typecode)

    # Fixup shape in case its empty or scalar.
    try:
        testVar = shape[0]
    except:
        shape = (0,)

    # Find the shape and set number of components.
    if len(shape) == 1:
        result_array.SetNumberOfComponents(1)
    else:
        result_array.SetNumberOfComponents(shape[1])

    result_array.SetNumberOfTuples(shape[0])

    # Ravel the array appropriately.
    arr_dtype = get_numpy_array_type(vtk_typecode)
    if numpy.issubdtype(z.dtype, arr_dtype) or \
       z.dtype == numpy.dtype(arr_dtype):
        z_flat = numpy.ravel(z)
    else:
        z_flat = numpy.ravel(z).astype(arr_dtype)
        # z_flat is now a standalone object with no references from the caller.
        # As such, it will drop out of this scope and cause memory issues if we
        # do not deep copy its data.
        deep = 1

    # Point the VTK array to the numpy data.  The last argument (1)
    # tells the array not to deallocate.
    result_array.SetVoidArray(z_flat, len(z_flat), 1)
    if deep:
        copy = result_array.NewInstance()
        copy.DeepCopy(result_array)
        result_array = copy
    else:
        result_array._numpy_reference = z
    return result_array


def get_vtk_array_type(numpy_array_type):
    """Returns a VTK typecode given a numpy array."""
    # This is a Mapping from numpy array types to VTK array types.
    _np_vtk = {numpy.uint8: vtkConstants.VTK_UNSIGNED_CHAR,
               numpy.uint16: vtkConstants.VTK_UNSIGNED_SHORT,
               numpy.uint32: vtkConstants.VTK_UNSIGNED_INT,
               numpy.uint64: vtkConstants.VTK_UNSIGNED_LONG_LONG,
               numpy.int8: vtkConstants.VTK_CHAR,
               numpy.int16: vtkConstants.VTK_SHORT,
               numpy.int32: vtkConstants.VTK_INT,
               numpy.int64: vtkConstants.VTK_LONG_LONG,
               numpy.float32: vtkConstants.VTK_FLOAT,
               numpy.float64: vtkConstants.VTK_DOUBLE,
               numpy.complex64: vtkConstants.VTK_FLOAT,
               numpy.complex128: vtkConstants.VTK_DOUBLE}
    for key, vtk_type in _np_vtk.items():
        if numpy_array_type == key or \
                numpy.issubdtype(numpy_array_type, key) or \
                numpy_array_type == numpy.dtype(key):
            return vtk_type
    raise TypeError(
        'Could not find a suitable VTK type for %s' % (str(numpy_array_type)))


def get_vtk_to_numpy_typemap():
    """Returns the VTK array type to numpy array type mapping."""
    _vtk_np = {vtkConstants.VTK_BIT: numpy.uint8,  # conversion not implemented
               vtkConstants.VTK_CHAR: numpy.int8,
               vtkConstants.VTK_SIGNED_CHAR: numpy.int8,
               vtkConstants.VTK_UNSIGNED_CHAR: numpy.uint8,
               vtkConstants.VTK_SHORT: numpy.int16,
               vtkConstants.VTK_UNSIGNED_SHORT: numpy.uint16,
               vtkConstants.VTK_INT: numpy.int32,
               vtkConstants.VTK_UNSIGNED_INT: numpy.uint32,
               # vtkConstants.VTK_LONG: LONG_TYPE_CODE,
               vtkConstants.VTK_LONG_LONG: numpy.int64,
               # vtkConstants.VTK_UNSIGNED_LONG: ULONG_TYPE_CODE,
               vtkConstants.VTK_UNSIGNED_LONG_LONG: numpy.uint64,
               # vtkConstants.VTK_ID_TYPE: ID_TYPE_CODE,
               vtkConstants.VTK_FLOAT: numpy.float32,
               vtkConstants.VTK_DOUBLE: numpy.float64}
    return _vtk_np
