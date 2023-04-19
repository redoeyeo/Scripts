from argparse import ArgumentParser

from notifypy import Notify


def main():
	parser = ArgumentParser()
	parser.add_argument('-t', '--title', type=str, required=True, help='Title of notification')
	parser.add_argument('-m', '--message', type=str, required=True, help='Message')
	parser.add_argument('-a', '--app', type=str, required=False, help='The app', default='notify.py')
	args = parser.parse_args()
	title = args.title
	message = args.message
	app = args.app

	notification = Notify()
	notification.application_name = app
	notification.title = title
	notification.message = message
	notification.send()


if __name__ == '__main__':
	main()
