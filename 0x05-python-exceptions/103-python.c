#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Prints basic info about Python lists.
 * @p: A PyObject list object.
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t x, xx, z;
	const char *s;
	PyListObject *a = (PyListObject *)p;
	PyVarObject *aa = (PyVarObject *)p;

	x = aa->ob_size;
	xx = a->allocated;

	fflush(stdout);

	printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "list") != 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	printf("[*] Size of the Python List = %ld\n", x);
	printf("[*] Allocated = %ld\n", xx);

	for (z = 0; z < x; z++)
	{
		s = a->ob_item[z]->ob_type->tp_name;
		printf("Element %ld: %s\n", z, s);
		if (strcmp(s, "bytes") == 0)
			print_python_bytes(a->ob_item[z]);
		else if (strcmp(s, "float") == 0)
			print_python_float(a->ob_item[z]);
	}
}

/**
 * print_python_bytes - Prints basic info about Python byte objects.
 * @p: A PyObject byte object.
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t x, z;
	PyBytesObject *a = (PyBytesObject *)p;

	fflush(stdout);

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", a->ob_sval);

	if (((PyVarObject *)p)->ob_size >= 10)
		x = 10;
	else
		x = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %ld bytes: ", x);
	for (z = 0; z < x; z++)
	{
		printf("%02hhx", a->ob_sval[z]);
		if (z == (x - 1))
			printf("\n");
		else
			printf(" ");
	}
}

/**
 * print_python_float - Prints basic info about Python float objects.
 * @p: A PyObject float object.
 */
void print_python_float(PyObject *p)
{
	char *a = NULL;

	PyFloatObject *float_obj = (PyFloatObject *)p;

	fflush(stdout);

	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	a = PyOS_double_to_string(float_obj->ob_fval, 'r', 0,
			Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", a);
	PyMem_Free(a);
}
