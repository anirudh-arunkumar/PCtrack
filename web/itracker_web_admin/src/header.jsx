import React from 'react';
import { Link } from 'react-router-dom';
import './header.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faHome, faBell, faCogs, faSignOutAlt } from '@fortawesome/free-solid-svg-icons'

class Header extends React.Component {
    constructor (props) {
        super(props);
        this.state = {};
        this.headers = [];
    }

    render () {
        return (
            <div className="container-fluid main-header">
                <div className="row">
                    <div className="col-md-3 left-menu">
                        <Link className="home_link" to="/">
                            iTracker
                        </Link>
                    </div>
                    <div className="col-md-6" />
                    <div className="col-md-3 right-menu">
                        <FontAwesomeIcon  className="header-menu-icon-button" icon={faBell}/>
                        <Link to="/settings">
                            <FontAwesomeIcon  className="header-menu-icon-button" icon={faCogs}/>
                        </Link>
                        <FontAwesomeIcon  className="header-menu-icon-button" icon={faSignOutAlt}/>
                    </div>
                </div>
            </div>
        );
    }
}

export default Header;
