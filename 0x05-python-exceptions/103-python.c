#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Here we go again
 * @p: another 5hrs to be wasted 
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t immensity, apportion, counter;
	const char *type;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	immensity = var->ob_size;
	apportion = list->allocated;

	fflush(stdout);

	printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "list") != 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	printf("[*] Size of the Python List = %ld\n", immensity);
	printf("[*] Allocated = %ld\n", apportion);

	for (counter = 0; counter < immensity; counter++)
	{
		type = list->ob_item[counter]->ob_type->tp_name;
		printf("Element %ld: %s\n", counter, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[counter]);
		else if (strcmp(type, "float") == 0)
			print_python_float(list->ob_item[counter]);
	}
}

/**
 * print_python_bytes - You have been f... haha
 * @p: come find me lads
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t immensity, counter;
	PyBytesObject *bytes = (PyBytesObject *)p;

	fflush(stdout);

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size >= 10)
		immensity = 10;
	else
		immensity = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %ld bytes: ", immensity);
	for (counter = 0; counter < immensity; counter++)
	{
		printf("%02hhx", bytes->ob_sval[counter]);
		if (counter == (immensity - 1))
			printf("\n");
		else
			printf(" ");
	}
}

/**
 * print_python_float - all this for what??
 * @p: is my future gonna be any better?
 */
void print_python_float(PyObject *p)
{
	char *buffer = NULL;

	PyFloatObject *float_obj = (PyFloatObject *)p;

	fflush(stdout);

	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	buffer = PyOS_double_to_string(float_obj->ob_fval, 'r', 0,
			Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", buffer);
	PyMem_Free(buffer);
}
