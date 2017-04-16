'use-strict';

import React from "react"

export default class LoginModal extends React.Component {
	constructor(props){
		super(props);
		this.state = {
			logdedIn : false,

		}
	}
	
	render() {
		if(!this.state.logdedIn)
		{
			return(
				<div className="container login-modal">
					<div className="login-text-color login-heading1">JIIT Portal</div>
					<div className="login-text-color"><span className="login-heading2">Welcome Back</span><br/><span className="login-heading3">Sign into your account.</span></div>
					<form>
						<div className="form-group login-input-field">
							<input type="text" className="form-control login-input-field-placeholder" placeholder="Enrollment Number"/>
						</div>
						<div className="form-group login-input-field">
							<input type="text" className="form-control login-input-field-placeholder" placeholder="DOB(dd-mm-yyyy)"/>
						</div>
						<div className="form-group login-input-field">
							<input type="password" className="form-control login-input-field-placeholder" placeholder="Password"/>
						</div>
					</form>
					<button className="btn btn-primary submit-button"><span>Submit</span></button>
					<div className="login-text-color login-heading3">
						<a>Forget Password?</a>
					</div>
				</div>
			)
		}
		else{
			return(
				<div>
					<h2>Successfully Logged in</h2>
				</div>
			)
		}
	}
}