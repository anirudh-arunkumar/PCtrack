import React from 'react';
import './page.css'
//import PageHeader from './pageheader';
//import ActiveProcessDash from './activeProcessDash';
//import ActiveProcessBrowse from './activeProcessBrowse';

class Page extends React.Component {
    constructor (props) {
        super(props);
        //console.log(this.props)
    }
    
    renderEmptyRoot = (props) => {
       //console.log(props.rconfig);
       return (
            <div className={props.rconfig.name}>
                {(props.rconfig.label === undefined) ? "" : <h4>{props.rconfig.label}</h4> }
                <props.rconfig.component {...props}/>
            </div>
        );
    }

    renderBranches = (props) => {
        return (
            <div className={props.rconfig.name}>
                <nav id="content-nav" className="navbar navbar-light bg-light px-3">
                    <a className="navbar-brand" href="#top">{props.rconfig.label}</a>
                    <ul className="nav nav-pills">
                        {
                            props.rconfig.branches.map((branch, i) => (
                                <li key={"branch"+i} className="nav-item">
                                    <a className="nav-link" href={"#"+branch.name}>{branch.label}</a>
                                </li>
                            ))
                        }
                    </ul>
                </nav>
                <div className="page-scrollpy" data-spy="scroll" data-target="#content-nav" data-offset="0" tabIndex="0">
                    {
                       props.rconfig.branches.map((branch, i) => (
                            <div key={'page'+i} className="page">
                                {i===0 ? <h4 id="top"/> : <h4 id={branch.name}>{branch.label}</h4>}
                                <branch.component {...props} branchConfig={branch}/>
                            </div>
                        ))
                    }
                </div>
            </div>
        );
    }

    render () {
        return (
            <div className="content-page">
                {this.props.rconfig.branches === undefined ? this.renderEmptyRoot(this.props) : this.renderBranches(this.props)}
            </div>
        );
    }

    /*render () {
        return (
            <div className="content-page">
                <PageHeader rconfig={this.props.rconfig}/>
                <this.props.rconfig.component {...this.props}/>
            </div>
        );
    }*/
};

export default Page;