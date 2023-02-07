from tkinter import *
import customtkinter
import pyautogui
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw
import PIL
from tkinter import filedialog
from tkinter import colorchooser

class Win:
	def __init__(self):
		self.WIDTH, self.HEIGHT = pyautogui.size()

		customtkinter.set_appearance_mode("dark")
		customtkinter.set_default_color_theme("dark-blue")

		self.image = Image.new(
			'RGB',
			(self.WIDTH, self.HEIGHT),
			'white'
			)
		self.draw = ImageDraw.Draw(self.image)

		self.root = customtkinter.CTk()
		self.root.geometry(f"{self.WIDTH}x{self.HEIGHT}")
		self.root.title("Paint")

		self.current_color = StringVar()

		self.current_color.set('black')
		self.my_color = self.current_color.get()

		self.canvas_color = StringVar()
		self.canvas_color.set('white')
		self.current_canvas_color = self.canvas_color.get()

		self.widgets()

	def chooseColor(self):
		self.color_code = colorchooser.askcolor(title = 'Choose Color')[1]
		self.current_color.set(self.color_code)
		self.my_color = self.current_color.get()

	def paint(self, event):
		x1, y1 = event.x - 1, event.y - 1
		x2, y2 = x1 + 1, y1 + 1

		self.BrushSize = self.chooseSize.get()

		self.canvas.create_rectangle(x1, y1, x2, y2, fill = self.my_color, outline = self.my_color, width = self.BrushSize)
		self.draw.rectangle([x1, y1, x2 + self.BrushSize, y2 + self.BrushSize], fill = self.my_color, outline = self.my_color, width = self.BrushSize)

	def new(self):
		self.canvas.delete('all')
		self.draw.rectangle([0, 0, self.WIDTH, self.HEIGHT], fill = self.current_canvas_color, outline = self.current_canvas_color)

	def clear(self):
		self.canvas.delete('all')
		self.draw.rectangle([0, 0, self.WIDTH, self.HEIGHT], fill = self.current_canvas_color, outline = self.current_canvas_color)

	def eraser(self):
		self.current_color.set(self.current_canvas_color)
		self.my_color = self.current_color.get()

	def save(self):
		filename = filedialog.asksaveasfilename(
			initialfile = 'untitled.png',
			defaultextension = 'png',
			filetypes = [('PNG', 'JPG'), ('.png', '.jpg')]
			)

		if filename != '':
			self.image.save(filename)

	def open(self):
		# filename = filedialog.askopenfilename(
		# 	initialfile = 'untitled.png',
		# 	filetypes = [('png', '*.png'), ('jpg', '*.jpg')]
		# 	)

		# img = ImageTk.PhotoImage(Image.open(filename))
		# self.canvas.create_image(10,10,anchor=NW,image=img)
		pass

	def widgets(self):
		self.menu = Menu(
			self.root,
			background='#0f0d0d',
			fg = '#5a68d6',
			activebackground = '#302626'
			)

		self.file_menu = Menu(
			self.menu,
			tearoff=False,
			background='#0f0d0d',
			fg = '#5a68d6',
			activebackground = '#302626'
			)

		self.file_menu.add_command(
			label = 'New',
			command = self.new
			)

		self.file_menu.add_command(
			label = 'Save',
			command = self.save
			)

		self.file_menu.add_command(
			label = 'Open',
			command = self.open
			)

		self.menu.add_cascade(
			label = 'File',
			menu = self.file_menu
			)

		self.root.config(menu = self.menu)

		self.canvas = customtkinter.CTkCanvas(
		self.root,
		width = self.WIDTH,
		height = self.HEIGHT,
		bg = self.current_canvas_color
		)

		self.canvas.place(x = 0, y = 100)

		self.chooseSize = customtkinter.CTkSlider(
			master = self.root,
			from_ = 0,
			to = 200,
			)
		self.chooseSize.grid(row = 0, column = 0)
		self.chooseSize.set(10)

		self.colorBtn = customtkinter.CTkButton(
			master = self.root,
			text = 'Choose Color',
			width = 200,
			height = 20,
			command = self.chooseColor
			)
		self.colorBtn.grid(row = 1, column = 0)

		self.canvas.bind('<B1-Motion>', self.paint)

		self.EraserBtn = customtkinter.CTkButton(
			master = self.root,
			text = 'Eraser',
			width = 200,
			height = 20,
			command = self.eraser
			)
		self.EraserBtn.grid(row = 0, column = 1)

		self.ClearBtn = customtkinter.CTkButton(
			master = self.root,
			text = 'Clear',
			width = 200,
			height = 20,
			command = self.clear
			)
		self.ClearBtn.grid(row = 1, column = 1)

		self.canvas.bind('<B1-Motion>', self.paint)
		self.canvas.bind('<Button-1>', self.paint)


win = Win()
win.root.mainloop()
