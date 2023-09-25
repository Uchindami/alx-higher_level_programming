#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - I'm I sure i want to push this?
 *
 * @p: Bcs i can get in trouble
 * Return: no return
 */
void print_python_bytes(PyObject *p)
{
	char *ligature;
	long int immensity, counter, ceiling;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	immensity = ((PyVarObject *)(p))->ob_size;
	ligature = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", immensity);
	printf("  trying string: %s\n", ligature);

	if (immensity >= 10)
		ceiling = 10;
	else
		ceiling = immensity + 1;

	printf("  first %ld bytes:", ceiling);

	for (counter = 0; counter < ceiling; counter++)
		if (ligature[counter] >= 0)
			printf(" %02x", ligature[counter]);
		else
			printf(" %02x", 256 + ligature[counter]);

	printf("\n");
}

/**
 * print_python_list - If i actually do this
 *
 * @p: 5 hrs be worth it??
 * Return: no return
 */
void print_python_list(PyObject *p)
{
	long int immensity, counter;
	PyListObject *list;
	PyObject *obj;

	immensity = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", immensity);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (counter = 0; counter < immensity; counter++)
	{
		obj = ((PyListObject *)p)->ob_item[counter];
		printf("Element %ld: %s\n", counter, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
