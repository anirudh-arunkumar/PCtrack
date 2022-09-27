import React from 'react';
import './App.css';
import Header from './header';
import {menulist} from './sidebarmenuitems';
import Sidebar from './sidebar';
import ContentArea from './contentarea';

class App extends React.Component {

  constructor (props) {
    super(props)
    this.state = {
      sidebar_expanded : false,
    }
  }

  onSidebarChange = (expanded) => {
    this.setState({sidebar_expanded: expanded})
  }

  render() {
    return (
      <div className="App main-panel">
        <Header/>
        <div className="main-body">
          <Sidebar depthStep={10} depth={0} items={menulist} onSidebarChange={this.onSidebarChange} />
          <ContentArea sidebar_state={this.state.sidebar_expanded} />
        </div>
      </div>
    );
  }
}

export default App;
