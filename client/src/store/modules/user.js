const state = {
  loggedIn: false,
  username: "",
  token: "",
};

const getters = {
  loggedIn: (state) => state.loggedIn,
  username: (state) => state.username,
  token: (state) => state.token,
};

const actions = {
  signIn({ commit }, payload) {
    console.log(arguments);
    commit("updateLoggedIn", true);
    commit("setUsername", payload.username);
    commit("setToken", payload.token);
  },
  signOut({ commit }) {
    commit("updateLoggedIn", false);
    commit("setUsername", "");
    commit("setToken", "");
  },
};

const mutations = {
  updateLoggedIn: (state, newStatus) => (state.loggedIn = newStatus),
  setUsername: (state, username) => (state.username = username),
  setToken: (state, token) => (state.token = token),
};

export default {
  state,
  getters,
  actions,
  mutations,
};
