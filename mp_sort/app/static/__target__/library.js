// Transcrypt'ed from Python, 2021-09-21 01:33:52
var random = {};
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __proxy__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, abs, all, any, assert, bool, bytearray, bytes, callable, chr, copy, deepcopy, delattr, dict, dir, divmod, enumerate, filter, float, getattr, hasattr, input, int, isinstance, issubclass, len, list, map, max, min, object, ord, pow, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
import * as __module_random__ from './random.js';
__nest__ (random, '', __module_random__);
var __name__ = '__main__';
export var array = [];
export var gen_random_int = function (number, seed) {
	random.seed (seed);
	var arr = (function () {
		var __accu0__ = [];
		for (var num = 0; num < number; num++) {
			__accu0__.append (num);
		}
		return __accu0__;
	}) ();
	random.shuffle (arr);
	return arr;
};
export var generate = function () {
	var number = 10;
	var seed = 200;
	array = gen_random_int (number, seed);
	var array_str = '';
	for (var num of array) {
		var num_str = str (num);
		var array_str = (array_str + ',') + num_str;
	}
	var array_str = array_str + '.';
	var array_str = array_str.__getslice__ (1, null, 1);
	document.getElementById ('generate').innerHTML = array_str;
};
export var sortnumber1 = function () {
	var array_new = array.__getslice__ (0, null, 1);
	print (array_new);
	var array_sort = sort_func (array_new);
	var array_str = '';
	for (var num of array_sort) {
		var num_str = str (num);
		var array_str = (array_str + ',') + num_str;
	}
	var array_str = array_str + '.';
	var array_str = array_str.__getslice__ (1, null, 1);
	document.getElementById ('sorted').innerHTML = array_str;
};
export var sortnumber2 = function () {
	var value = document.getElementsByName ('numbers') [0].value;
	if (value == '') {
		window.alert ('Your textbox is empty');
		return ;
	}
	var arr = (function () {
		var __accu0__ = [];
		for (var val of value.py_split (',')) {
			__accu0__.append (val.strip ());
		}
		return __accu0__;
	}) ();
	var arr = (function () {
		var __accu0__ = [];
		for (var el of arr) {
			__accu0__.append (int (el));
		}
		return __accu0__;
	}) ();
	var array_sort = sort_func (arr);
	var array_str = '';
	for (var num of array_sort) {
		var num_str = str (num);
		var array_str = (array_str + ',') + num_str;
	}
	var array_str = array_str + '.';
	var array_str = array_str.__getslice__ (1, null, 1);
	document.getElementById ('sorted').innerHTML = array_str;
};
export var sort_func = function (arr) {
	var n = len (arr);
	var swap = true;
	while (swap == true) {
		var swap = false;
		var new_n = 0;
		for (var inner_iter = 1; inner_iter < n; inner_iter++) {
			var first_num = arr [inner_iter - 1];
			var second_num = arr [inner_iter];
			if (second_num < first_num) {
				arr [inner_iter] = first_num;
				arr [inner_iter - 1] = second_num;
				print (arr);
				var swap = true;
				var new_n = inner_iter;
			}
		}
		var n = new_n;
	}
	return arr;
};

//# sourceMappingURL=library.map