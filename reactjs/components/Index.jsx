'use-strict';

import React from "react"
import { render } from "react-dom"
import LoginModal from "./LoginModal"

class Index extends React.Component {
  render() {
    return(
    	<div className="login">
    	<p>jhfd</p>
    	<h1>jsdfkdsngfjkdsnfjs</h1>
    	<LoginModal/>
    	</div>)
  }
}

render(<Index/>, document.getElementById('Index'))