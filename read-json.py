# import pandas

# read = pandas.read_json('data.json')

# print(read.to_string())



# create dataframe using json 
import pandas

result = {
	"Math": {
		"John": 90,
		"Watson": 86,
		"Shine": 77,
		"Wile": 87
	},
	"DSA": {
		"John": 56,
		"Watson": 99,
		"Shine": 45,
		"Wile": 86
	},
	"Physics": {
		"John": 55,
		"Watson": 78,
		"Shine": 98,
		"Wile": 56
	},
	"Web Mastering": {
		"John": 93,
		"Watson": 66,
		"Shine": 55,
		"Wile": 87
	}
}

show = pandas.DataFrame(result)
print(show)