import React from "react";
import List from "@material-ui/core/List";
import ListItem from "@material-ui/core/ListItem";
import Divider from "@material-ui/core/Divider";

import ExpandMoreIcon from "@material-ui/icons/ExpandMore";
import ExpandLessIcon from "@material-ui/icons/ExpandLess";
import Collapse from "@material-ui/core/Collapse";
import { Link } from 'react-router-dom';

class SidebarItem extends React.Component {

    constructor (props) {
        super(props);
        this.state = {
            collapsed: true
        }

        //console.log(this.props);
    }

    toggleCollapse = () => {
      this.setState(prevState => ({
        collapsed: !prevState.collapsed
      }));
    }

    onClick = (e) => {
        if (Array.isArray(this.props.item.items)) {
          this.toggleCollapse();
        }
        if (this.props.onClickProp) {
          this.props.onClickProp(e, this.props.item);
        }
    }
    
    expandIcon = () => {
        let expandIcon;
      
        if (Array.isArray(this.props.item.items) && this.props.item.items.length) {
          expandIcon = !this.state.collapsed ? (
            <ExpandLessIcon
              className={
                "sidebar-item-expand-arrow sidebar-item-expand-arrow-expanded"
              }
            />
          ) : (
            <ExpandMoreIcon className="sidebar-item-expand-arrow" />
          );
        }

        return expandIcon;
    }
  
    render_colapsed_sidebar = () => {
      const { label, items, Icon, onClick: onClickProp, path } = this.props.item;

      return (
          <>
              <ListItem
                  className="sidebar-item"
                  onClick={this.onClick}
                  button
                  dense
                  {...this.props.rest}
                  component={Link}
                  to={path}
                  >
              <div
                  style={{ paddingLeft: this.props.depth * this.props.depthStep }}
                  className="sidebar-item-content"
              >
                  {Icon && <Icon className="sidebar-item-icon" fontSize="small" />}
              </div>
              </ListItem>
              <Collapse in={!this.state.collapsed} timeout="auto" unmountOnExit>
              {Array.isArray(items) ? (
                  <List disablePadding dense>
                  {items.map((subItem, index) => (
                      <React.Fragment key={`${subItem.name}${index}`}>
                      {subItem === "divider" ? (
                          <Divider style={{ margin: "6px 0" }} />
                      ) : (
                          <SidebarItem
                          depth={this.props.depth + 1}
                          depthStep={this.props.depthStep}
                          item={subItem}
                          />
                      )}
                      </React.Fragment>
                  ))}
                  </List>
              ) : null}
              </Collapse>
          </>
        );
    }

    render_default_sidebar = () => {
      const { label, items, Icon, onClick: onClickProp, path } = this.props.item;

      return (
          <>
              <ListItem
              className="sidebar-item"
              onClick={this.onClick}
              button
              dense
              {...this.props.rest}
              component={Link}
              to={path}
              >
              <div
                  style={{ paddingLeft: this.props.depth * this.props.depthStep }}
                  className="sidebar-item-content"
              >
                  {Icon && <Icon className="sidebar-item-icon" fontSize="small" />}
                  <div className="sidebar-item-text">{label}</div>
              </div>
              {this.expandIcon()}
              </ListItem>
              <Collapse in={!this.state.collapsed} timeout="auto" unmountOnExit>
              {Array.isArray(items) ? (
                  <List disablePadding dense>
                  {items.map((subItem, index) => (
                      <React.Fragment key={`${subItem.name}${index}`}>
                      {subItem === "divider" ? (
                          <Divider style={{ margin: "6px 0" }} />
                      ) : (
                          <SidebarItem
                          depth={this.props.depth + 1}
                          depthStep={this.props.depthStep}
                          sidebar_expanded={this.props.sidebar_expanded}
                          item={subItem}
                          />
                      )}
                      </React.Fragment>
                  ))}
                  </List>
              ) : null}
              </Collapse>
          </>
        );
    }
    

    render() {
        return (
          this.props.sidebar_expanded?this.render_default_sidebar():this.render_colapsed_sidebar()
        );
    }
  }

  export default SidebarItem;