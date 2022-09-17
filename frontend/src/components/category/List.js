import React, { Component } from 'react';
import { connect } from 'react-redux';
import { PropTypes } from 'prop-types';
import { getCategories, deleteCategory, toggleCategory } from '../../actions/categories';

import { Fragment } from 'react';

class List extends Component {

  static propTypes = {
    categories: PropTypes.array.isRequired,
    getCategories: PropTypes.array.isRequired,
    toggleCategory: PropTypes.array.isRequired,
    deleteCategory: PropTypes.array.isRequired
  };

  componentDidMount() {
    this.props.getCategories();
  };

  render() {
    return (
      <Fragment>
        <h2>Sub_categories list</h2>
        {this.props.categories.map(ThirdCategory => (
          <ul key={ThirdCategory.id}>
            <li>{ThirdCategory.name}</li>
            <li>{ThirdCategory.sub_categories}</li>
            <li><button onChange={this.props.toggleCategory.bind(this, ThirdCategory)}>Change</button></li>
            <li><button onClick={this.props.deleteCategory.bind(this, ThirdCategory.id)}>Delete</button></li>
          </ul>
        ))}
      </Fragment>
    )
  }
}


const mapStateToProps = (state) => ({
  categories: state.categories.categories
});

export default connect(mapStateToProps, { getCategories, deleteCategory, toggleCategory })(List);
