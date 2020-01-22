<template>
  <v-app id="inspire">
    <v-navigation-drawer
      v-model="drawer"
      app
      clipped
    >
      <v-list dense>
        <v-list-item
          v-for="(item, i) in items"
          :key="i"
          @click="route(item.routeName)"
          link
        >
          <v-list-item-action >
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>
              {{ item.text }}
            </v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-subheader class="mt-4 grey--text text--darken-1">REVIEWERS</v-subheader>
        <v-list>
          <v-list-item
            v-for="(item, i) in reviewer_list"
            :key="i"
            link
          >
            <v-list-item-avatar>
              <img
                :src="`https://randomuser.me/api/portraits/men/33.jpg`"
                alt=""
              >
            </v-list-item-avatar>
            <v-list-item-title v-text="item.Name" />
          </v-list-item>
        </v-list>
        <v-list-item class="mt-4" link v-show="$store.state.username">
          <v-list-item-action>
            <v-icon color="grey darken-1">mdi-account-outline</v-icon>
          </v-list-item-action>
          <v-list-item-title class="grey--text text--darken-1">Welcome, {{currentUser}}</v-list-item-title>
        </v-list-item>
        <v-list-item link href="">
          <v-list-item-action>
            <v-icon color="grey darken-1">mdi-settings</v-icon>
          </v-list-item-action>
          <v-list-item-title class="grey--text text--darken-1">Management</v-list-item-title>
        </v-list-item>
        <v-list-item link @click="$store.commit('switch2Admin')">
          <v-list-item-action>
            <v-icon color="grey darken-1">mdi-cctv</v-icon>
          </v-list-item-action>
          <v-list-item-title class="grey--text text--darken-1">Admin View</v-list-item-title>
        </v-list-item>
        <v-list-item link >
          <v-list-item-action @click="$store.commit('switch2Reviewer')">
            <v-switch v-model="reviewer" label="" ></v-switch>
          </v-list-item-action>
          <v-list-item-title class="grey--text text--darken-1">Reviewer View</v-list-item-title>
        </v-list-item>
        <v-list-item link href="http://localhost:8080/" v-show="$store.state.username">
          <v-list-item-action>
            <v-icon color="grey darken-1">mdi-logout</v-icon>
          </v-list-item-action>
          <v-list-item-title class="grey--text text--darken-1">Log Out</v-list-item-title>
        </v-list-item>
        
      </v-list>
    </v-navigation-drawer>

    <v-app-bar
      app
      clipped-left
      color="red"
      dense
    >
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
      <v-icon class="mx-4">fab fa-youtube</v-icon>
      <v-toolbar-title class="mr-12 align-center">
        <span class="title">Escalation Assistant</span>
      </v-toolbar-title>
      <v-spacer />
      <v-row
        align="center"
        style="max-width: 650px"
      >
        <v-text-field
          :append-icon-cb="() => {}"
          placeholder="Search..."
          single-line
          append-icon="mdi-magnify"
          color="white"
          hide-details
        />
      </v-row>
    </v-app-bar>

    <v-content>
      <v-container class="fill-height">
        <v-row
          justify="center"
          align="center"
        >
        <router-view></router-view>
        </v-row>
        
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
  export default {
    props: {
      source: String,
    },
    data: () => ({
      drawer: null,
      reviewer: false,
      items: [
        { icon: 'mdi-format-list-bulleted-square', text: 'DashBoard', routeName: 'Dashboard' },
        // { icon: 'mdi-signal-variant', text: 'Subscriptions', routeName: 'Dashboard' },
        { icon: 'mdi-email', text: 'E-mail', routeName: 'Dashboard' },
        { icon: 'mdi-account-multiple-outline', text: 'Create Meeting', routeName: 'Dashboard' },
        { icon: 'mdi-history', text: 'Previous Comments', routeName: 'PreviousComments' },
      ],
      items2: [
        { picture: 28, text: 'Joseph' },
        { picture: 38, text: 'Apple' },
        { picture: 48, text: 'Xbox Ahoy' },
        { picture: 58, text: 'Nokia' },
        { picture: 78, text: 'MKBHD' },
      ],
    }),
    created () {
      this.$vuetify.theme.dark = true
    },
    asyncComputed: {
      reviewer_list: {
          async get() {
              try {
                  const res = await this.$http.get(`http://127.0.0.1:8000/escBackend/reviewer/`)
                  this.reviewer_cnt = res.data.length
                  return res.data
              }catch(e) {
                  window.console.log(e)
              }
          }
      }
    },
    methods: {
      route(path) {
        this.$router.push({name: path})
      }
    },
    computed: {
      currentUser() {
        return this.$store.state.username
      }
    }
  }
</script>