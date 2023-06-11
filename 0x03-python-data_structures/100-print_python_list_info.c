#include <Python.h>

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: input needed list
 */

void print_python_list_info(PyObject *p)
{
	int a, s, x;
	PyObject *z;

	a = Py_SIZE(p);
	s = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %d\n", a);
	printf("[*] Allocated = %d\n", s);
	for (x = 0; x < a; x++)
	{
		printf("Element %d: ", x);
		z = PyList_GetItem(p, x);
		printf("%s\n", Py_TYPE(z)->tp_name);
	}
}
