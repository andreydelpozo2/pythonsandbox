#include <Python.h>


static PyObject * spam_system(PyObject* self, PyObject *args)
{
	const char* command;
	int sts;

	if(!PyArg_ParseTuple(args, "s", &command))
	{
		return NULL;
	}

	sts = system(command);
	return Py_BuildValue("i",sts);
}

static PyObject *SpamError;

static PyMethodDef SpamMethods[] = {
	{"system", spam_system, METH_VARARGS, "Execute a shell command"},
	{NULL,NULL,0,NULL}
};

PyMODINIT_FUNC initspam(void)
{
	PyObject *m;
	 m = Py_InitModule("spam", SpamMethods);	
	 if(m == NULL)
	 	return;

	 SpamError = PyErr_NewException("Spam.Error",NULL,NULL);
	 Py_INCREF(SpamError);
	 PyModule_AddObject(m, "error", SpamError);
}