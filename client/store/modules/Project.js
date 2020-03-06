import taskLists from "./TaskLists";

const state = { name: "No Current project" };

const getters = {
  fetchProject: () => {
    //fetch the actual project
    return { name: "project" };
  }
};

const actions = {
  fetchProject({ commit }) {
    //perform API call to fetch project
    commit("fetch");
  }
};

const mutations = {};

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations,
  modules: {
    taskLists
  }
};
