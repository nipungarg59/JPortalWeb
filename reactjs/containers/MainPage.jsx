'use-strict';

import React from 'react';
import { connect } from 'react-redux'
import LoginModal from "./LoginModal"

class MainPage extends React.Component {
	constructor(props){
		super(props);
	}
	
	render() {
		return(
			<div className="container-fluid login">
			<LoginModal/>
			</div>)
	}
}

function mapStateToProps(state){
	//retrieval in this component as this.props.(login or whtever) 
	return {
		login: false
	}
}

export default connect(mapStateToProps)(MainPage)