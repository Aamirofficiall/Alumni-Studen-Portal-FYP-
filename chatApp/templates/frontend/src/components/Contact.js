import { NavLink } from "react-router-dom";
import axios from "axios";
import React, { Component } from 'react'

export class Contact extends Component {
  state = {
    
    chat: [],
    id:null
    
  }  
   replaceAll=(string, search, replace)=> {
    return string.split(search).join(replace);
  }
  getName = () => {

    var itemNO = this.props.chatURL.split('_').length
    var name = this.props.chatURL
    // name = name.replace(localStorage.getItem('username'), '')
    name = this.replaceAll(name,'_',' ')
    // name = name.replace('_', ' ')
    var username = localStorage.getItem('username')
    if (username !== null & username !== undefined)
    {
      username = localStorage.getItem('username').charAt(0).toUpperCase() + username.slice(1)  
      }
      
    name = name.replace(username, '')
    // if (name.length > 18)
    // {
    //   name = name.slice(0, 18)
    //   name += ' ... '
    //   // name+='[Group]'
    // }
    if (itemNO > 2)
    {
      name+=' [Group]'
    }

   
    return name
  }
  render() {
    return (
      <div>
        
                
                <NavLink to={`/${this.props.chatURL}`} style={{ color: "#fff" }}>      
                <li className="contact">
                  {localStorage.getItem('token') !== null ?
              
                  <div className="wrap">        
                    <span className={`contact-status ${this.props.status}`} />
                    <img src={this.props.picURL} alt="" />
                    <div className="meta">
                  <p className="name" >   
                  {console.log(localStorage.getItem('name'))}
                    {this.getName()}
                    </p>
                      
                    </div>
                  </div>
                    :
              <p></p>
              
              
                  }
              
                  
          </li>

          </NavLink>
      </div>
    )
  }
}


export default Contact;
