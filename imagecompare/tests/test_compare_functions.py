from imagecompare.src.model import Model
import csv

def test_parse_csv():
	"""Tests if the model.parse_csv() method correctly parses the input CSV file."""
	testList = [['image1', 'image2'],
		['./imagecompare/tests/test_images/newtoe.jpg', './imagecompare/tests/test_images/notoe.jpg'],
		['./imagecompare/tests/test_images/rain.png', './imagecompare/tests/test_images/notoe.jpg'],
		['./imagecompare/tests/test_images/test.png', './imagecompare/tests/test_images/test.png'],
		['./imagecompare/tests/test_images/g1.png', './imagecompare/tests/test_images/g2.png'],
		['./imagecompare/tests/test_images/g1.png', './imagecompare/tests/test_images/g3.png'],
		['./imagecompare/tests/test_images/rain.png', './imagecompare/tests/test_images/rain.png']]
	
	model = Model()
	fileList = model.parse_csv('./imagecompare/tests/test_csv/test.csv')
	assert fileList == testList


def test_compare_valid_images():
	"""Tests comparison score of all valid images against known values."""
	testList = [['image1', 'image2'],
		['./imagecompare/tests/test_images/newtoe.jpg', './imagecompare/tests/test_images/notoe.jpg'],
		['./imagecompare/tests/test_images/rain.png', './imagecompare/tests/test_images/notoe.jpg'],
		['./imagecompare/tests/test_images/test.png', './imagecompare/tests/test_images/test.png'],
		['./imagecompare/tests/test_images/g1.png', './imagecompare/tests/test_images/g2.png'],
		['./imagecompare/tests/test_images/g1.png', './imagecompare/tests/test_images/g3.png'],
		['./imagecompare/tests/test_images/rain.png', './imagecompare/tests/test_images/rain.png']]
	correctComparison = ['0.01814', '1', '0', '0.00001', '0.00003', '0']

	model = Model()
	i = 0
	for img1, img2 in testList[1:]:
		result = model.compare_images(img1,img2)
		assert result[0] == correctComparison[i]
		if result[0] != '1':
			assert float(result[1]) > 0
		else:
			assert float(result[1]) == 0.0
		i += 1

def test_compare_with_invalid_images():
	"""Tests comparison score of all valid images and files that do not exist images against known values."""
	testList = [['image1', 'image2'],
		['./imagecompare/tests/test_images/aa.png', './imagecompare/tests/test_images/ab.png'],
		['./imagecompare/tests/test_images/ab.png', './imagecompare/tests/test_images/bb.jpg'],
		['./imagecompare/tests/test_images/test.png', './imagecompare/tests/test_images/test.png'],
		['./imagecompare/tests/test_images/bc.png', './imagecompare/tests/test_images/g2.png'],
		['./imagecompare/tests/test_images/g1.png', './imagecompare/tests/test_images/g3.png'],
		['./imagecompare/tests/test_images/rain.png', './imagecompare/tests/test_images/rain.png']]
	correctComparison = ['File Not Found', 'File Not Found', '0', 'File Not Found', '0.00003', '0']

	model = Model()
	i = 0
	for img1, img2 in testList[1:]:
		result = model.compare_images(img1,img2)
		assert result[0] == correctComparison[i]

		if result[0] != '1':
			assert float(result[1]) >= 0.0
		elif result[0] == 'File Not Found':
			assert float(result[1]) == 0.0
		i += 1

def test_output_csv_format():
	"""Tests the model.write_csv() method to check if file is correct, as well as the location"""
	testList = [['image1','image2'],
		['./imagecompare/tests/test_images/aa.png','./imagecompare/tests/test_images/ba.png'],
		['./imagecompare/tests/test_images/g1.png', './imagecompare/tests/test_images/g3.png'],
		['./imagecompare/tests/test_images/ab.png','./imagecompare/tests/test_images/bb.png'],
		['./imagecompare/tests/test_images/test.png','./imagecompare/tests/test_images/test.png'],
		['./imagecompare/tests/test_images/ac.png','./imagecompare/tests/test_images/bc.png'],
		['./imagecompare/tests/test_images/ad.png','./imagecompare/tests/test_images/bd.png'],
		['./imagecompare/tests/test_images/newtoe.jpg','./imagecompare/tests/test_images/notoe.jpg'],
		['./imagecompare/tests/test_images/ac.png','./imagecompare/tests/test_images/bc.png']]

	postComparisonPairs = [['File Not Found','0'], ['0.00003','0.08757'], ['File Not Found','0'], ['0','0.08542'],
						['File Not Found','0'], ['File Not Found','0'], ['0.01814','7.76046'], ['File Not Found','0']]

	correctResultList = [['image1', 'image2', 'similar', 'elapsed'],
						['./imagecompare/tests/test_images/aa.png', './imagecompare/tests/test_images/ba.png', 'File Not Found', '0'],
						['./imagecompare/tests/test_images/g1.png', './imagecompare/tests/test_images/g3.png', '0.00003', '0.08757'],
						['./imagecompare/tests/test_images/ab.png', './imagecompare/tests/test_images/bb.png', 'File Not Found', '0'],
						['./imagecompare/tests/test_images/test.png', './imagecompare/tests/test_images/test.png', '0', '0.08542'],
						['./imagecompare/tests/test_images/ac.png', './imagecompare/tests/test_images/bc.png', 'File Not Found', '0'],
						['./imagecompare/tests/test_images/ad.png', './imagecompare/tests/test_images/bd.png', 'File Not Found', '0'],
						['./imagecompare/tests/test_images/newtoe.jpg', './imagecompare/tests/test_images/notoe.jpg', '0.01814', '7.76046'],
						['./imagecompare/tests/test_images/ac.png', './imagecompare/tests/test_images/bc.png', 'File Not Found', '0']]

	model = Model()

	filename = model.write_csv('./imagecompare/tests/test_csv/test.csv', testList, postComparisonPairs)

	assert filename == './imagecompare/tests/test_csv/out_file.csv'
	
	with open(filename, 'r') as csv_obj:
		csv_reader = csv.reader(csv_obj)

		csvList = []
		for line in csv_reader:
			csvList.append(line)

	assert csvList[0] == ['image1','image2','similar','elapsed']

	i = 1
	for line in csvList[1:]:
		assert line[0] == correctResultList[i][0]
		assert line[1] == correctResultList[i][1]
		assert line[2] == correctResultList[i][2]
		assert float(line[3]) >= 0.0

		i+=1


