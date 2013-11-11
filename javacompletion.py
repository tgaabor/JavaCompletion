import sublime, sublime_plugin, os, re, threading, urllib
from xml.etree import ElementTree as ET
from urllib.request import urlopen

GOOGLE_AC = r"http://google.com/complete/search?output=toolbar&q=%s"

class GoogleAutocomplete(sublime_plugin.EventListener):
	def on_query_completions(self, view, prefix, locations):
		if prefix != '':
			elements = ET.parse(urlopen(GOOGLE_AC % prefix)).getroot().findall("./CompleteSuggestion/suggestion")
			sugs = [(x.attrib["data"],) * 2 for x in elements]
			return sugs
		return ([], sublime.INHIBIT_EXPLICIT_COMPLETIONS)


class ExampleCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.insert(edit, 0, "Hello, World!")

# ============================== Method class ==============================
class Method:
	_name = ""
	_signature = ""
	_filename = ""

	def __init__(self, name, signature, filename):
		self._name = name
		self._signature = signature
		self._filename = filename

	def name(self):
		return self._name

	def signature(self):
		return self._signature

	def filename(sefl):
		return self._filename

# ================== MethodSignatureCollectorThread class ==================
class MethodSignatureCollectorThread(threading.Thread):

	_search_path = '/Users/Gabor/Devel'

	def __init__(self):
		# init class
		threading.Thread.__init__(self)

	def run(self):
		print('run')

	def stop(self):
		if self.isActive():
			self._Thread__stop()

class MethodSignatureCollector(sublime_plugin.EventListener):

	_collector_thread = None

	def on_query_completions(self, view, prefix, locations):
		current_file = view.file_name()
		print('futok: ' + current_file + ' prefix: ' + prefix)
		completions = ([["alm333a", "alm333a"], ["korte", "korte"], ["current_file", current_file]], sublime.INHIBIT_WORD_COMPLETIONS)
		#completions = ["alm333a", "korte", current_file]
		#completions = ((x) * 2 for x in completions, sublime.INHIBIT_WORD_COMPLETIONS)
		if current_file.endswith('.java') or current_file.endswith('.py'):
			print('java file')
			return completions
		return (completions, sublime.INHIBIT_EXPLICIT_COMPLETIONS)



