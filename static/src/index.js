import React from 'react';
import ReactDOM from 'react-dom';

import { Provider } from 'react-redux'
import store from './store'
import Landing from './components/landing'
import Header from './components/header'

ReactDOM.render(
    <Provider store={store}>
        <Header/>
        <Landing/>
    </Provider>,
    document.getElementById('app')
);

module.hot.accept();
