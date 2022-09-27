import React from 'react';
import { Redirect, Route, Switch } from 'react-router-dom';
import './contentarea.css';

import {RouteConfigList} from './routeconfig';
import ErrorPage from './error';

import Page from './page';

function BuildRoute(route) {
    return (
      <Route
        path={route.path}
        render={ props => (
            <Page {...props} rconfig={route} local_settings={route.local_settings}/>
        )}
      />
    );
}

class ContentArea extends React.Component {
    constructor (props) {
        super(props);
        this.state = {
            open: false
        };

        this.headers = [];

        //console.log(props);
    }

    render () {
        var collapsed_style = {
            'marginLeft': '64px'
        };
    
        var expanded_style = {
            'marginLeft': '240px'
        };

        return (
            <div id="main-content" style={this.props.sidebar_state?expanded_style:collapsed_style}>
                <div className="main-content">
                    <Switch>
                        <Route exact path='/' 
                                render={() => {
                                    return (<Redirect to="/main" />);
                                }} 
                        />
                        {
                            RouteConfigList.map((route, i) => (
                                <Route key={route+i}
                                    path={route.path}
                                    render={ props => (
                                        <Page {...props} rconfig={route} local_settings={this.props.local_settings}/>
                                    )}
                                />
                            ))
                        }
                        <Route component={ErrorPage} />
                    </Switch>
                </div>
            </div>
        );
    }
}

export default ContentArea;
