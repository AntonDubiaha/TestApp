import axios from 'axios';
import { GET_CATEGORY_LIST, DELETE_CATEGORY, ADD_CATEGORY, PUT_CATEGORY } from '../actions/types';

axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN';
axios.defaults.xsrfCookieName = 'csrftoken';

export const getCategories = () => dispatch => {
    axios.get('api/sub_categories/')
        .then(result => {
            dispatch({
                type: GET_CATEGORY_LIST,
                payload: result.data
            });
        }).catch(error => console.log(error));
};

export const deleteCategory = (id) => dispatch => {
    axios.delete(`api/sub_categories/${id}/`)
        .then(result => {
            dispatch({
                type: DELETE_CATEGORY,
                payload: id
            });
        }).catch(error => console.log(error));
};

export const putCategory = (ThirdCategory) => dispatch => {
    axios.put(`api/sub_categories/${ThirdCategory.id}/`, ThirdCategory)
        .then(result => {
            dispatch({
                type: PUT_CATEGORY,
                payload: result.data
            });
        }).catch(error => console.log(error));
};

export const addCategory = (ThirdCategory) => dispatch => {
    axios.post('api/sub_categories/', ThirdCategory)
        .then(result => {
            dispatch({
                type: ADD_CATEGORY,
                payload: result.data
            });
        }).catch(error => console.log(error));
};