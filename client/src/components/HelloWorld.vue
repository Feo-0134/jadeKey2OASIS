<template>
  <v-app id="inspire">
    <v-navigation-drawer
      v-model="drawer"
      app
      clipped
    >
      <v-list dense>
        <v-list-item link>
          <v-list-item-action>
            <v-icon>mdi-view-dashboard</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Dashboard</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item link>
          <v-list-item-action>
            <v-icon>mdi-settings</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Settings</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar
      app
      clipped-left
    >
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
      <v-toolbar-title>Jade_Key</v-toolbar-title>
    </v-app-bar>

    <v-content>
      <v-container
        class="fill-height"
        fluid
      >
        <v-row
          justify="center"
        >
        <!-- <p>{{process_list}}</p> -->
        <Process v-for="(p, index) in process_list" :key="p._id"
        :pindex="index" :process="p"
        > </Process>
        </v-row>
      
      </v-container>
    </v-content>

    <v-footer app>
      <span>&copy; 2019</span>
    </v-footer>
  </v-app>
</template>

<script>
  import Process from '@/components/Process'
  export default {
    components: {Process},
    props: {
      source: String,
    },
    data: () => ({
      drawer: null,
      e1: 1,
      detailShow: false,
      user: 2
    }),
    asyncComputed: {
      process_list: {
        async get() {
          try {
            const res = await this.$http.get(`http://127.0.0.1:8000/escapp/engineer/${this.user}/process_list`);
            // console.log(res)
            return res.data
          }catch(e) {
            // console.log(e);
          }
        }
      }
    },
    created () {
      this.$vuetify.theme.dark = true
    },
  }
</script>