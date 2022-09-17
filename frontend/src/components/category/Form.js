import React, { Component } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { addCategory } from '../../actions/categories';

class Form extends Component {

    state = {
        name: '',
        sub_categories: ''
    };

    static propTypes = {
      addCategory: PropTypes.func.isRequired
    };

    onSubmit = (e) => {
        e.preventDefault();
        const { name, sub_categories } = this.state;
        const category = { name, sub_categories };
        this.props.addCategory(category);
        this.setState({
            name: '',
            sub_categories: ''
        });
    };

    onChange = (e) => this.setState({ [e.target.name]: e.target.value });

    render() {
        const { name, sub_categories } = this.state;

        return (
            <div className='card card-body mt-4 mb-4'>
                <h2>Add sub_categories</h2>
                <form onSubmit={this.onSubmit}>
                    <div className='form-group'>
                        <label>Name</label>
                        <input
                            type='text'
                            className='form-control'
                            name='name'
                            onChange={this.onChange}
                            value={name} />
                    </div>
                    <div className='form-group'>
                        <label>Second category id</label>
                        <input
                            type='text'
                            className='form-control'
                            name='sub_categories'
                            onChange={this.onChange}
                            value={sub_categories} />
                    </div>
                    <div className='form-group'>
                        <button type='submit' className='btn btn-primary'>Add</button>
                    </div>
                </form>
            </div>
        )
    }
}

export default connect(null, { addCategory })(Form);