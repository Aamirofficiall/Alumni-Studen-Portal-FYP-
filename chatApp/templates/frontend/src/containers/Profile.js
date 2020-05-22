import React from "react";
import { connect } from "react-redux";
import { Redirect } from "react-router-dom";
import Hoc from "../hoc/hoc";
import { createStore } from 'redux'


class Profile extends React.Component {
  // getUsername = () => {
  //   var temp=this.props.chats.memebers_name
  //   if (temp !== undefined) {
  //     var name = temp
  //     var ans = "";
  //     var words = temp.split("_");

  //     for (var i = 0; i < words.length; i++) {
  //       words[i] = words[i].charAt(0).toUpperCase() + words[i].slice(1);
  //       ans += words[i]
  //     }
  //     console.log(asn)
  //   }
  // }

  replaceAll=(string, search, replace)=> {
    return string.split(search).join(replace);
  }
  getUserName = () => {
    var itemNO = this.props.id.split('_').length

    var name = this.props.id
    // name = name.replace(localStorage.getItem('username'), '')
    name = this.replaceAll(name,'_',' ')
    // name = name.replace('_', ' ')
    var username = localStorage.getItem('username')
    if (username !== null & username !== undefined)
    {
      username = localStorage.getItem('username').charAt(0).toUpperCase() + username.slice(1)  
      }
      name = name.replace(username, '')
   
      if (itemNO > 2)
      {
        name+=' [Group]'
      }
  
     
      return name
  }

  state = {
    loc:''
  }
  
  render() {
    if (this.props.token === null) {
      return <Redirect to="/" />;
    }
    return (
      <div className="contact-profile">
        {this.props.username !== null ? (
          <Hoc>
            <img src="http://emilcarlsson.se/assets/harveyspecter.png" alt="" />
            {this.state.loc}
            <p>{this.getUserName()}</p>
            <div className="social-media">
              
              <i className="fa fa-facebook" aria-hidden="true" />
              <i className="fa fa-twitter" aria-hidden="true" />
              <i className="fa fa-instagram" aria-hidden="true" />
            </div>
          </Hoc>
        ) : null}
      </div>
    );
  }
}

const mapStateToProps = state => {
  return {
    token: state.auth.token,
    username: state.auth.username,
    chats: state.message.chats,
    
  };
};

const mapDispatchToProps = dispatch => {
  return {
    getUserChats: (username, token) =>
      dispatch(messageActions.getUserChats(username, token)),
    getChats: () => {
      
      // return window.location.pathname
    }
    
  };
};


export default connect(mapStateToProps)(Profile);
