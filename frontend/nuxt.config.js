/*!

 =========================================================
 * Nuxt Black Dashboard - v1.0.0
 =========================================================

 * Product Page: https://www.creative-tim.com/product/nuxt-black-dashboard
 * Copyright 2020 Creative Tim (https://www.creative-tim.com)

 * Coded by Creative Tim

 =========================================================

 * The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
 */
export default {
  mode: 'debug',
  /*
  ** Headers of the page
  */
  head: {
    title: 'RocketERP',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: process.env.npm_package_description || '' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.png' },
      { rel: 'stylesheet', href: 'https://fonts.googleapis.com/css?family=Poppins:200,300,400,600,700,800'},
      { rel: 'stylesheet', href: 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.10.2/css/all.min.css'}
    ],
    bodyAttrs: {
      class: '' // Add `white-content` class here to enable "white" mode.
    }
  },
 router: {
    middleware: 'router-auth'
  },
  /*
  ** Customize the progress-bar color
  */
  loading: { color: '#fff' },
  /*
   ** Global CSS
   */
  css: [
    'assets/css/demo.css',
    'assets/css/nucleo-icons.css',
    'assets/sass/black-dashboard.scss'
  ],
  /*
  ** Plugins to load before mounting the App
  */

  plugins: [
    '~/plugins/dashboard-plugin.js',
    '~/plugins/axios.js'
  ],

  /*
  ** Nuxt.js dev-modules
  */
  buildModules: [],
  /*
  ** Nuxt.js modules
  */
  modules: [
    '@nuxtjs/pwa',
    'nuxt-i18n',
    '@nuxtjs/axios',
     '@nuxtjs/auth',

  ],
  i18n: {
    locales: [
      {
        code: 'en',
        file: 'ru.js'
      },
      {
        code: 'ru',
        file: 'ru.js'
      }
    ],
    lazy: true,
    langDir: 'lang/',
    defaultLocale: 'en',
  },

 axios: {
    baseURL: 'http://127.0.0.1:8000',
    browserBaseURL: 'http://127.0.0.1:8000'
  },
  auth: {
    fetchUserOnLogin: true,
    strategies: {
      local: {
        endpoints: {
          login: { url: '/api/v1/auth/jwt/', method: 'post', propertyName: 'access' },
          logout: { url: '/api/v1/auth/jwt/logout/', method: 'post' },
          user: { url: '/api/v1/auth/profile/', propertyName: false },
        },
        tokenType: 'JWT',
        tokenName: 'Authorization'
      }
    },
    redirect: {
      login: '/login',
      home: '/'
    }
  },



  /*
  ** Build configuration
  */
  build: {
    transpile: [/^element-ui/],
    /*
    ** You can extend webpack config here
    */
    extend (config, ctx) {
    },
    babel: {
      plugins: [
        [
          'component',
          {
            'libraryName': 'element-ui',
            'styleLibraryName': 'theme-chalk'
          }
        ]
      ]
    }
  }
}
