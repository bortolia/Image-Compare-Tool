from imagecompare.src.model import Model

def test_parse_csv():
	correctList = [['image1', 'image2'],
		['./imagecompare/tests/test_images/newtoe.jpg', './imagecompare/tests/test_images/notoe.jpg'],
		['./imagecompare/tests/test_images/rain.png', './imagecompare/tests/test_images/notoe.jpg'],
		['./imagecompare/tests/test_images/test.png', './imagecompare/tests/test_images/test.png'],
		['./imagecompare/tests/test_images/g1.png', './imagecompare/tests/test_images/g2.png'],
		['./imagecompare/tests/test_images/g1.png', './imagecompare/tests/test_images/g3.png'],
		['./imagecompare/tests/test_images/rain.png', './imagecompare/tests/test_images/rain.png']]
	
	model = Model()
	fileList = model.parse_csv('./imagecompare/tests/test_csv/test.csv')
	assert fileList == correctList


def test_compare_images():
	correctList = [['image1', 'image2'],
		['./imagecompare/tests/test_images/newtoe.jpg', './imagecompare/tests/test_images/notoe.jpg'],
		['./imagecompare/tests/test_images/rain.png', './imagecompare/tests/test_images/notoe.jpg'],
		['./imagecompare/tests/test_images/test.png', './imagecompare/tests/test_images/test.png'],
		['./imagecompare/tests/test_images/g1.png', './imagecompare/tests/test_images/g2.png'],
		['./imagecompare/tests/test_images/g1.png', './imagecompare/tests/test_images/g3.png'],
		['./imagecompare/tests/test_images/rain.png', './imagecompare/tests/test_images/rain.png']]
	correctComparison = ['0.01814', '1', '0', '0.00001', '0.00003', '0']

	model = Model()
	i = 0
	for img1, img2 in correctList[1:]:
		result = model.compare_images(img1,img2)
		assert result[0] == correctComparison[i]
		if result[0] != '1':
			assert float(result[1]) > 0
		else:
			assert float(result[1]) == 0.0
		i += 1

