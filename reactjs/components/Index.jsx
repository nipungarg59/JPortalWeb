'use-strict';

import React from "react"
import { render } from "react-dom"
import MainPage from "../containers/MainPage"

import {
  createStore,
  compose,
  applyMiddleware,
  combineReducers,
} from "redux"
import { Provider } from "react-redux"
import reducers from "../reducers/Index"

const createStoreWithMiddleware = applyMiddleware()(createStore);

class Index extends React.Component {
	render() {
		return(
			<Provider store={createStoreWithMiddleware(reducers)}>
				<MainPage/>
			</Provider>
		)
  	}
}


render(<Index/>, document.getElementById('Index'))