# Introduction

React/React Redux/Webpack/Material UI Frontend.

## Quickstart
Build the project via:
```console
npm install
npm build
```

## Structure
- React/React Redux code can be found in `src`.
- Redux reducers and actions have their own respective folders.
- Components are found in the `components` directory. Each component has its own folder.
- CSS files are found in the `styles` folder.
- `index.html` and other assets are located in the `public` folder.

## NPM commands

NPM commands can be found in `package.json`.

- `npm build`: builds the project for localhost development.
- `npm watch`: watches for changes, continuously builds for localhost development.
- `npm prod`: builds the product targeting the AWS URL, which is specified in `webpack.prod.js`
