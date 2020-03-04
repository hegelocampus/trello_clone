import Vue from 'vue';
import Vuex from 'vuex';

import mutations from './mutations.js';

Vue.use(Vuex)

const debug = process.env.NODE_ENV !== 'production'

export default new Vuex.Store({
  state: {
    project: {
      name: 'No Current project',
      allTasks: defaultTasks
    }
  },
  mutations,
  strict: true,
  plugins: []
})
