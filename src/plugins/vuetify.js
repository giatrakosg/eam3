import Vue from 'vue';
import Vuetify from 'vuetify/lib';
import colors from 'vuetify/lib/util/colors'

Vue.use(Vuetify);

export default new Vuetify({
  theme: {
  themes: {
    light: {
      primary: colors.blue.darken3,
      secondary: colors.blue.lighten5,
      accent: colors.shades.black,
      error: colors.red.accent3,
    },
    dark: {
      primary: colors.blue.lighten3,
    },
  },
},
});
