import { createStore } from 'vuex';
import axios from 'axios';

const store = createStore({
  state: {
    token: localStorage.getItem('token') || '',
    user_id: "",
    username: localStorage.getItem('username') || '',
    isAuthenticated: false,
    cart: []
  },
  mutations: {
    initializeStore(state){
      if (localStorage.getItem('token')) {
        state.token = localStorage.getItem('token');
        state.user_id = localStorage.getItem('user_id');
        state.username = localStorage.getItem('username');
        state.isAuthenticated = true;
      } else {
        state.token = "";
        state.user_id = "";
        state.username = '';
        state.isAuthenticated = false;
      }
    },
    setToken(state, payload){
      console.log("setting token:", payload.token, 'User ID:', payload.user_id, 'username:', payload.username);
      state.token = payload.token;
      state.user_id = payload.user_id;
      state.username = payload.username;
      localStorage.setItem('token', payload.token);
      localStorage.setItem('user_id', payload.user_id);
      localStorage.setItem('username', payload.username);
      state.isAuthenticated = true;
    },
    removeToken(state,user_id){
      state.token = "";
      state.user_id= "";
      state.username = '';
      localStorage.removeItem('token');
      localStorage.setItem('user_id',user_id);
      localStorage.removeItem('username');
      state.isAuthenticated = false;
    },
    setCart(state, cart){
      state.cart = cart;
    },
    addToCart(state, ejemplar){
      state.cart.push(ejemplar);
    },
    removeFromCart(state, ejemplarId){
      state.cart = state.cart.filter(item => item.id !== ejemplarId);
    }
  },
  actions: {
    async login({ commit }, credentials) {
      try {
        const response = await axios.post('http://127.0.0.1:8000/api/login/', credentials);
        const { token, user } = response.data;
        commit('setToken', { token, user_id: user.id, username: user.username});
        localStorage.setItem('token', token);
        localStorage.setItem('user_id', user.id);
        localStorage.setItem('username', user.username);
      } catch (error) {
        console.error('Login error:', error.response ? error.response.data : error.message);
      }
    },
    logout({commit}){
      commit('removeToken');
      localStorage.removeItem('token');
      localStorage.removeItem('user_id');
      localStorage.removeItem('username');
    },
    async fetchCart({ commit, state }) {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/carritos/', {
          headers: {
            Authorization: `Token ${state.token}`
          }
        });
        commit('setCart', response.data);
      } catch (error) {
        console.error('Error fetching cart:', error);
      }
    },
    async addToCart({ commit, state }, ejemplar) {
      try {
          const response = await axios.post('http://127.0.0.1:8000/api/carritos/', {
              ejemplar: [ejemplar.id] 
          }, {
              headers: {
                  Authorization: `Token ${state.token}`
              }
          });
          commit('addToCart', response.data);
      } catch (error) {
          console.error('Error adding ejemplar to cart:', error);
      }
    },
    async removeFromCart({ commit, state }, ejemplarId) {
      try {
        await axios.delete(`http://127.0.0.1:8000/api/carritos/${ejemplarId}/`, {
          headers: {
            Authorization: `Token ${state.token}`
          }
        });
        commit('removeFromCart', ejemplarId);
      } catch (error) {
        console.error('Error removing from cart:', error);
      }
    }
  },
  getters: {
    isAuthenticated: state => state.isAuthenticated,
    username: state => state.username,
    cartItems: state => state.cart
  }
});

export default store;