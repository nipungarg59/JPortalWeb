'use-strict';

import React from "react"
import { render } from "react-dom"
import LoginModal from "./LoginModal"

class Index extends React.Component {
  render() {
    return(
    	<div className="container-fluid login">
    	<LoginModal/>
    	</div>)
  }
}

render(<Index/>, document.getElementById('Index'))