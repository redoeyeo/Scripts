import pyperclip
import sys


def main():
	try:
		command = sys.argv[1]
	except IndexError:
		command = 'unknown'
	if command == 'paste':
		print(pyperclip.paste())
	elif command == 'copy':
		text = ' '.join(sys.argv[2:])
		pyperclip.copy(text)
	else:
		raise RuntimeError('Valid commands: paste or copy')


if __name__ == '__main__':
	main()
