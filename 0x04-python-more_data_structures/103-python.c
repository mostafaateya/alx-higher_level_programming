#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - prints some basic info about Python bytes
 * @p: Python object
 * Return: void
 */

void print_python_bytes(PyObject *p)
{
	char *s;
	long int x, y, z;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("   [ERROR] Invalid Bytes Object\n");
		return;
	}
	x = ((PyVarObject *)(p))->ob_size;
	s = ((PyBytesObject *)p)->ob_sval;
	printf("   size: %ld\n", x);
	printf("   trying string: %s\n", s);
	if (x >= 10)
		z = 10;
	else
		z = x + 1;
	printf("   first %ld bytes:", z);
	for (y = 0; y < z; y++)
		if (s[y] >= 0)
			printf(" %02x", s[y]);
		else
			printf(" %02x", 256 + s[y]);
	printf("\n");
}

/**
 * print_python_list - prints some basic info about Python lists
 * @p: Python Object
 * Return: void
 */

void print_python_list(PyObject *p)
{
	long int x, y;
	PyListObject *a;
	PyObject *b;

	x = ((PyVarObject *)(p))->ob_size;
	a = (PyListObject *)p;
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", x);
	printf("[*] Allocated = %ld\n", a->allocated);
	for (y = 0; y < x; y++)
	{
		b = ((PyListObject *)p)->ob_item[y];
		printf("Element %ld: %s\n", y, ((b)->ob_type)->tp_name);
		if (PyBytes_Check(b))
			print_python_bytes(b);
	}
}
