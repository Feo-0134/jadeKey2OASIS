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

          <v-stepper v-model="e1">

              <v-stepper-header>
              <v-avatar color="indigo" size="48" style="margin:auto">
                <span class="white--text headline">GM</span>
              </v-avatar>
                <v-stepper-step :complete="e1 > 1" step="1">Step 1</v-stepper-step>

                <v-divider></v-divider>

                <v-stepper-step :complete="e1 > 2" step="2">Step 2</v-stepper-step>

                <v-divider></v-divider>

                <v-stepper-step :complete="e1 > 3" step="3">Step 3</v-stepper-step>

                <v-divider></v-divider>

                <v-stepper-step  step="4">Step 4</v-stepper-step>
                
                <v-icon @click='detailShow=!detailShow'>mdi-chevron-down</v-icon>
              </v-stepper-header>

              <v-stepper-items v-show="detailShow">
                <v-stepper-content step="1">
                  <v-card
                    class="mb-12"
                    color="grey lighten-1"
                    height="200px"
                  ></v-card>

                  <v-btn color="primary"
                    @click="e1 = 2"
                  >
                    Continue
                  </v-btn>

                  <v-btn text>Cancel</v-btn>
                </v-stepper-content>

                <v-stepper-content step="2">
                  <v-card
                    class="mb-12"
                    color="grey lighten-1"
                    height="200px"
                  ></v-card>

                  <v-btn
                    color="primary"
                    @click="e1 = 3"
                  >
                    Continue
                  </v-btn>

                  <v-btn text>Cancel</v-btn>
                </v-stepper-content>

                <v-stepper-content step="3">
                  <v-card
                    class="mb-12"
                    color="grey lighten-1"
                    height="200px"
                  ></v-card>

                  <v-btn
                    color="primary"
                    @click="e1 = 4"
                  >
                    Continue
                  </v-btn>

                  <v-btn text>Cancel</v-btn>
                </v-stepper-content>
                <v-stepper-content step="4">
                  <v-card
                    class="mb-12"
                    color="grey lighten-1"
                    height="200px"
                  ></v-card>

                  <v-btn
                    color="primary"
                    @click="e1 = 1"
                  >
                    Continue
                  </v-btn>

                  <v-btn text>Cancel</v-btn>
                </v-stepper-content>
              </v-stepper-items>
          </v-stepper>
          <!-- <v-stepper v-model="e2">
              <v-stepper-header>
                <v-stepper-step :complete="e1 > 1" step="1">Step 1</v-stepper-step>

                <v-divider></v-divider>

                <v-stepper-step :complete="e1 > 2" step="2">Step 2</v-stepper-step>

                <v-divider></v-divider>

                <v-stepper-step :complete="e1 > 3" step="3">Step 3</v-stepper-step>

                <v-divider></v-divider>

                <v-stepper-step  step="4">Step 4</v-stepper-step>
                
                <v-icon @click='detailShow=!detailShow'>mdi-chevron-down</v-icon>
              </v-stepper-header>

              <v-stepper-items v-show="detailShow">
                <v-stepper-content step="1">
                  <v-card
                    class="mb-12"
                    color="grey lighten-1"
                    height="200px"
                  ></v-card>

                  <v-btn color="primary"
                    @click="e1 = 2"
                  >
                    Continue
                  </v-btn>

                  <v-btn text>Cancel</v-btn>
                </v-stepper-content>

                <v-stepper-content step="2">
                  <v-card
                    class="mb-12"
                    color="grey lighten-1"
                    height="200px"
                  ></v-card>

                  <v-btn
                    color="primary"
                    @click="e1 = 3"
                  >
                    Continue
                  </v-btn>

                  <v-btn text>Cancel</v-btn>
                </v-stepper-content>

                <v-stepper-content step="3">
                  <v-card
                    class="mb-12"
                    color="grey lighten-1"
                    height="200px"
                  ></v-card>

                  <v-btn
                    color="primary"
                    @click="e1 = 4"
                  >
                    Continue
                  </v-btn>

                  <v-btn text>Cancel</v-btn>
                </v-stepper-content>
                <v-stepper-content step="4">
                  <v-card
                    class="mb-12"
                    color="grey lighten-1"
                    height="200px"
                  ></v-card>

                  <v-btn
                    color="primary"
                    @click="e1 = 1"
                  >
                    Continue
                  </v-btn>

                  <v-btn text>Cancel</v-btn>
                </v-stepper-content>
              </v-stepper-items>
          </v-stepper> -->
      
        </v-row>
      
      </v-container>
    </v-content>

    <v-footer app>
      <span>&copy; 2019</span>
    </v-footer>
  </v-app>
</template>

<script>
  export default {
    props: {
      source: String,
    },
    data: () => ({
      drawer: null,
      e1: 1,
      detailShow: false,
    }),
    created () {
      this.$vuetify.theme.dark = true
    },
  }
</script>