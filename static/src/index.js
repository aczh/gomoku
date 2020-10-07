import React from 'react';
import ReactDOM from 'react-dom';

import { Provider } from 'react-redux'
import store from './store'
import Board from './components/board'

const title = 'React with Webpack and Babel';

ReactDOM.render(
    <Provider store={store}>
        <Board/>
    </Provider>,
    document.getElementById('app')
);

module.hot.accept();
