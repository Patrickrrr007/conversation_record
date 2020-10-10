#對話紀錄

def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig')as f:
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	Allens_text = 0
	Allens_pictures = 0
	Allens_stickers = 0
	Vikis_text = 0
	Vikis_pictures = 0
	Vikis_stickers = 0
	# person = None #先宣告無 避免如果person沒有人當掉的情況
	
	for line in lines:
			s = line.split(' ')
			time = s[0]
			name = s[1]
			if name == 'Allen':
				if s[2] == '圖片':
					Allens_pictures += 1
				elif s[2] == '貼圖':
					Allens_stickers += 1
				else: 
					for Atc in s[2:]:
						Allens_text += len(Atc)
			elif name == 'Viki':
				if s[2] == '圖片':
					Vikis_pictures += 1
				if s[2] == '貼圖':
					Vikis_stickers += 1
				else:
					for Vtc in s[2:]:
						Vikis_text += len(Vtc)

	print('Allen的圖片數：', Allens_pictures)
	print('Viki的圖片數：', Vikis_pictures)
	print('Allen講的字數：', Allens_text)
	print('Viki講的字數：', Vikis_text)
	print('Allen的貼圖數：', Allens_stickers)
	print('Viki的貼圖數數：', Vikis_stickers)

def write_file(filename, lines):
	with open(filename, 'w')as f:
		for line in lines:
			f.write(line + '\n')



def main():
	lines = read_file('LINE-Viki.txt')
	lines = convert(lines)
		# write_file('output.txt', lines)

main()

