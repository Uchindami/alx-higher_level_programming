#include <Python.h>

/**
 * print_python_list_info - this will print out our python buddies
 * @p: Eyetu Python Object list.
 */
void print_python_list_info(PyObject *p)
{
	int immensity, apportion, counter;
	PyObject *obj;

	immensity = Py_SIZE(p);
	apportion = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", immensity);
	printf("[*] Allocated = %d\n", apportion);

	for (counter = 0; counter < immensity; i++)
	{
		printf("Element %d: ", counter);

		obj = PyList_GetItem(p, counter);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
