
# Migrating JavaScript to TypeScript

  * TypeScript is great, but incremental migration is even better
  * Steps:
    * Adding typescript config and webpack
	* Adding type declaration files
	* Convert the code into typescript

---

## Install packages

  * We need `webpack` as package bundler, `typescript` as compiler for `*.ts`, and type declarations for external packages.
  * Here, take `cesium` for example

```bash
npm install --save-dev webpack typescript cesium @types/cesium
```

---

## Adding typescript config

  * Add typescript config `tsconfig.json`

```json
{
    "compilerOptions": {
        "target": "es5",
        "module": "commonjs",
        "noImplicitAny": true,
        "lib": [
        "es5","es2015", "es6", "dom"
        ]
    }
}
```

---

## Setup webpack

```javascript
var path = require('path');
var webpack = require('webpack');

module.exports = {
  entry: {
    index: "./index.ts"
  },
  target: 'node',
  module: {
    loaders: [
      { test: /\.ts(x?)$/, loader: 'ts-loader' },
      { test: /\.json$/, loader: 'json-loader' }
    ]
  },
  plugins: [
    new webpack.DefinePlugin({'process.env.NODE_ENV': '"production"'})
    ],
  resolve: {
    extensions: ['.ts', '.js', '.json']
  },
  output: {
    libraryTarget: 'commonjs',
    path: path.join(__dirname, 'lib'),
    filename: '[name].js'
  },
};
```

---

## References

  * [Incrementally Migrating JavaScript to TypeScript](https://medium.com/@clayallsopp/incrementally-migrating-javascript-to-typescript-565020e49c88)
  * [Converting a JavaScript project to Typescript, one file at a time](https://dev.to/suhas_chatekar/converting-a-javascript-project-to-typescript-one-file-at-a-time)
