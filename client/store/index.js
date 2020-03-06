import Vue from "vue";
import Vuex from "vuex";

import project from "./modules/Project";

Vue.use(Vuex);

//const debug = process.env.NODE_ENV !== "production";

export default new Vuex.Store({
  state: {},
  strict: true,
  modules: {
    project
  },
  plugins: []
});
