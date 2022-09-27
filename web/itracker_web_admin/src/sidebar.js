import React from "react";
import List from "@material-ui/core/List";
import ListItem from "@material-ui/core/ListItem";
import Divider from "@material-ui/core/Divider";
import CloseIcon from '@material-ui/icons/Close';
import DehazeIcon from '@material-ui/icons/Dehaze';
import './sidebar.css';
import SidebarItem from './sidebarItem.js'
  
  class Sidebar extends React.Component {
    constructor (props) {
      super(props);
      this.state = {
          open: true,
          expanded: false,
          selecte: 'home'
      }
    }

    onClick = (e) => {
      this.setState(prevState => ({
        expanded: !prevState.expanded
      }));

      //This is a hack
      //need to think of a better way to handle this.
      this.props.onSidebarChange(!this.state.expanded);
    }

    render() {
      
      const items =  this.props.items; 
      const depthStep = this.props.depthStep;
      const depth = this.props.depth; 
      const menuexpanded = this.props.expanded;

      var collapsed_style = {
        'minWidth': '64px'
      };

      var expanded_style = {
        'minWidth': '240px'
      };

        return (
          <div className="sidebar" style={this.state.expanded?expanded_style:collapsed_style}>
            <List disablePadding dense>
              <ListItem
                className="sidebar-control"
                onClick={this.onClick}
                button
              >
                <div
                  style={{ paddingLeft: depth * depthStep }}
                  className="sidebar-item-content"
                >
                  {this.state.expanded? <CloseIcon className="sidebar-item-icon" fontSize="small" />
                    : <DehazeIcon className="sidebar-item-icon" fontSize="small" />}
                </div>
                
              </ListItem>

              {items.map((sidebarItem, index) => (
                <React.Fragment key={`${sidebarItem.name}${index}`}>
                  {sidebarItem === "divider" ? (
                    <Divider style={{ margin: "6px 0" }} />
                  ) : (
                    <SidebarItem
                      depthStep={depthStep}
                      depth={depth}
                      itemexpanded={menuexpanded}
                      sidebar_expanded={this.state.expanded}
                      item={sidebarItem}
                    />
                  )}
                </React.Fragment>
              ))}
            </List>
          </div>
        );
    }
  }
  
  export default Sidebar;