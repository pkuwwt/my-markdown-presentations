
# js-xlsx USAGE

  * [SheetJS](https://sheetjs.com/) is one of the best options for front-end operation of Excel and similar 2D tables
  * [js-xlsx](https://github.com/SheetJS/sheetjs) is the community version
  * `js-xlsx` focuses on data transformation and export
  * `js-xlsx` supports a wide variety of data parsing, exporting and manipulating, not limited to xlsx format
  * `js-xlsx` supports both browser (javascript) and server (node.js) sides
  * For server side (node.js), it supports reading and writing with streaming supported.

---

## Concept

  * `js-xlsx` provides an intermediate layer for abstraction and manipulation, which represents the spreadsheet data as a single JS object. So the users don't have to handle different types of complex data types.
  * It also provides a series of abstract functions for this object.
  * The difference between browser and server side is about the files. Other data operations are the same.


---


## Introduce the library

  * For browser

```html
<script lang="javascript"
	src="https://cdnjs.cloudflare.com/ajax/libs/xlsx/0.15.4/xlsx.full.min.js">
</script>
```

  * For node.js
    * Install: `npm install xlsx --save`
	* Import: `const xlsx = require('xlsx');`

---

## Correspondence relationship

  * The type correspondence

| Excel    | Abstract types in `js-xlsx` |
| :------ | :------------------------- |
| workbook | workBook |
| WorkSheet| Sheets |
| Excel Reference Style (Cell Address) | cellAddress |
| Cell | cell|

  * The operation correspondence

```javascript
// open a workbook
const workbook = xlsx.readFileSync('data.xlsx');
// Get the worksheet name in the workbook
const first_sheet = workbook.SheetNames [0];
// Provides a reference style (cell subscript)
const cellAddress ='A1';
// Get the corresponding worksheet object
const worksheet = workbook.Sheets[first_sheet];
// Gets the corresponding cell object
const cell = worksheet[cellAddress];
// Get the data in the corresponding cell
const value = desired_cell ? cell.v: undefined;
```

---

## Data format

  * A data structure of a workbook
    * Directory, Workbook, Props, Custprops, Deps, Sheets, SheetNames, Strings, Styles, Themes, SSF
  * Once the file is parsed, all in the table will be parsed synchronously. And we can access the data using keys directly.
  * There are two commonly used properties:
    * `SheetNames`: the array of names of all worksheets
	* `Sheets`: an object with keys from `SheetNames` and sheet values
  * Excel's data units are sorted from small to large as: cell, worksheet, workbook?

---

## Format cells

  * In Excel, cells have multiple formats, and `js-xlsx` parses them to corresponding JavaScript format

| key of cell data | description | 
| :--------------: | :-----------------: |
| v | source data (unprocessed data) |
| w | Formated text (if formatted) |
| t | Cell type (see table below for specific types) |
| r | Decoded rich text (if it can be decoded) |
| h | Render rich text in HTML format (if decodable) |
| c | Cell annotations |
| z | Numbers formatted into strings (if needed) |

  * For example, the data stored in cell `A1` with content `xm` as follows:

```
A1: Object {t: "s", v: "xm", r: "<t>xm</t>", w: "xm", h: "xm"}
```

---

## Cell address

  * There are two ways to describe cell areas in an operation: cell address objec, cell range
    * cell address object
```javascript
const start = { c: 0, r: 0 }; // start cell with column and row indices
const end = { c: 1, r: 1 };   // end cell with column and row indices
	```
	* cell range
```javascript
const range = 'A1:B2'; // Excel style range
```

---

## API

  * There are two main categories of the `js-xlsx` functionality
    * Functions of the object itself for
	  * Analitical data
	  * Derived data
	* Tools in `utils`
	  * Adding data to data table objects
	  * Converting 2D arrays and formatted objects or HTML to worksheet objects
	  * Converting a workbook to another data format
	  * Transcoding and decoding between rows, columns, ranges
	  * Workbook operation
	  * Cell operation

---

### Read the data and parse it
  * Simple example in node.js
```javascript
const xlsx = require('xlsx');
const {readFileSync} = require('fs');
const buffer = readFileSync('./books.xlsx');
const result = xlsx.read(buffer, {type: 'buffer', cellHTML: false});
// or equivalently
const result2 = xlsx.readFileSync('./books.xlsx');
```

---

### Create new workbook

```javascript
const xlsx = require('xlsx');
const workbook = xlsx.utils.book_new();
const ws_data = [
	['S', 'h', 'e', 'e', 't', 'J', 'S'],
	[1, 2, 3, 4, 5]
];
const worksheet = xlsx.utils.aoa_to_sheet(ws_data);
xlsx.utils.book_append_sheet(workbook, worksheet, 'worksheet name');
```

---

### Data filling

  * There are many ways to manipulate data. There are the most common ones
    * Create worksheets using existing data structures: 2D array, JSON
	* Modify worksheet data: 2D array, JSON
---

#### Create worksheets using existing data structures

  * From 2D array

```javascript
const worksheet = xlsx.utils.aoa_to_sheet(
		[[1,2,3,new Date()],[1,2,,4], {
			sheetStubs: false, cellStyles: false, cellDates: true
		});
```

  * From JSON

```javascript
const worksheet = xlsx.utils.json_to_sheet([
		{'Column 1': 1,'Column 2': 2,'Column 3': 3},
		{'Column 1': 4,'Column 2': 5,'Column 3': 6}
],{
	Header: ['Column 1','Column 2','Column 3'],
	SkpHeader: true // skip the title line above
});
```

---

#### Modify data table

  * With 2D array

```javascript
xlsx.utils.sheet_add_aoa(worksheet, [
    [7,8,9],
    ['A','B','C']
],{
    Origin:'A1'// Add content from A1
});
```

  * With JSON

```javascript
xlsx.utils.sheet_add_json(worksheet,[
    {'Column 1': 7,'Column 2': 8,'Column 3': 9},
    {'Column 1':'A','Column 2':'B','Column 3':'C'}
],{
    Origin:'A1', // Add content from A1
    Header: ['Column 1','Column 2','Column 3'],
    SkipHeader: true // skip the title line above
});
```

---

## Data export

  * There are two steps for exporting
    * Converting workbook objects to other data structures
	  * `sheet_to_csv`, `sheet_to_dif`, `sheet_to_eth`, `sheet_to_formulae`, `sheet_to_html`, `sheet_to_json`, `sheet_to_slk`, `sheet_to_txt`, `sheet_set_array_formula`

	* Write to file

```javascript
const result xlsx.write(workbook, {
    BookType: 'xlsx', // file type
	Type: 'buffer',   // data type
	Compression: true // zip
});
fs.writeFileSync('./out.xlsx', result);
```
---

## References

  * [SheetJS js-xlsx module learning guide](https://developpaper.com/sheetjs-js-xlsx-module-learning-guide/)

