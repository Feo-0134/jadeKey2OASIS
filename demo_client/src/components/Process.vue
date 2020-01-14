<template>
    <v-container>
        <!-- {{ process_object }} -->
        <v-card>
            <v-app-bar dark color="red">

            <v-toolbar-title>{{process_title}}</v-toolbar-title>

            <v-spacer></v-spacer>

    <v-dialog
      v-model="dialog"
      width="500">
      <template v-slot:activator="{ on }">
        <v-btn icon v-on="on">
                <v-icon>mdi-account-edit-outline</v-icon>
            </v-btn>
      </template>

      <v-card>
        <v-card-title
          class="headline grey lighten-2"
          primary-title
          color="blue"
        >
          Privacy Policy
        </v-card-title>

        <v-card-text>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="primary"
            text
            @click="dialog = false"
          >
            I accept
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
            </v-app-bar>

            <v-container>
            <v-row dense>
                <v-col
                align="center"
                justify="center"
                v-for="(item, i) in items"
                :key="i"
                cols="12"
                >
                <v-card
                    :color="item.color"
                    dark
                >
                    <div class="d-flex flex-no-wrap justify-space-between">
                    <div>
                        <v-card-title
                        class="headline"
                        v-text="stage_list[i].FullName"
                        >
                        </v-card-title>

                        <v-card-subtitle v-text="item.artist">
                        </v-card-subtitle>            
                    </div>
                        <div class="headline ma-3"
                        size="25"
                        tile>
                        <v-icon>
                            mdi-window-close
                        </v-icon>
                        {{process_tryTimes[i]}}
                        </div>
                    <!-- <v-avatar
                        class="ma-2"
                        size="100"
                        tile
                    >
                        <v-img :src="item.src"></v-img>
                    </v-avatar> -->
                    </div>
                </v-card>
                <v-icon class="my-3" x-large=true>
                    mdi-timeline-clock-outline
                </v-icon>
                </v-col>
                <v-col cols="12">
                <v-card
                    color="#385F73"
                    dark
                >
                    <v-card-title class="headline">Review Complete</v-card-title>

                    <v-card-subtitle>More detail about this process.</v-card-subtitle>
                </v-card>
                </v-col>
            </v-row>
            </v-container>
        </v-card>
        <v-timeline
        :align-top="alignTop"
        :dense="dense"
        :reverse="reverse">
        <v-timeline-item
            v-for="n in 3"
            :key="n"
            :fill-dot="fillDot"
            :hide-dot="hideDot"
            :icon="icon ? 'mdi-star' : ''"
            :icon-color=" iconColor ? 'deep-orange' : ''"
            :left="left"
            :right="right"
            :small="small"
        >
            <template v-slot:icon>
            <v-avatar v-if="avatar">
                <img src="http://i.pravatar.cc/64">
            </v-avatar>
            </template>
            <span slot="opposite">Tus eu perfecto</span>
            <v-card class="elevation-2">
            <v-card-title class="headline">Lorem ipsum</v-card-title>
            <v-card-text>
                Lorem ipsum dolor sit amet, no nam oblique veritus. Commune scaevola imperdiet nec ut, sed euismod convenire principes at. Est et nobis iisque percipit, an vim zril disputando voluptatibus, vix an salutandi sententiae.
            </v-card-text>
            </v-card>
        </v-timeline-item>
        </v-timeline>
        <!-- <v-radio-group row wrap>
        <v-switch v-model="alignTop" label="Toggle align-top" class="mx-4"></v-switch>
        <v-switch v-model="dense" label="Toggle dense" class="mx-4"></v-switch>
        <v-switch v-model="fillDot" label="Toggle fill-dot" class="mx-4"></v-switch>
        <v-switch v-model="hideDot" label="Toggle hide-dot" class="mx-4"></v-switch>
        <v-switch v-model="icon" label="Toggle icon" class="mx-4"></v-switch>
        <v-switch v-model="avatar" label="Toggle avatar" class="mx-4"></v-switch>
        <v-switch v-model="iconColor" label="Toggle icon color" class="mx-4"></v-switch>
        <v-switch v-model="reverse" label="Toggle reverse" class="mx-4"></v-switch>
        <v-switch v-model="left" label="Toggle left" class="mx-4"></v-switch>
        <v-switch v-model="right" label="Toggle right" class="mx-4"></v-switch>
        <v-switch v-model="small" label="Toggle small" class="mx-4"></v-switch>
        </v-radio-group> -->
    </v-container>
</template>
<script>
export default {
    props: {
        process_object: Object
    },
    components: {},
    data: () => ({
        stage_cnt: 0,
        alignTop: false,
        avatar: false,
        dense: true,
        fillDot: false,
        hideDot: false,
        icon: false,
        iconColor: false,
        left: false,
        reverse: false,
        right: false,
        small: false,
        items: [
            {
            color: '#1F7087',
            src: 'https://cdn.vuetifyjs.com/images/cards/foster.jpg',
            title: 'Submit Request',
            artist: 'Foster the People',
            },
            {
            color: '#952175',
            src: 'https://cdn.vuetifyjs.com/images/cards/halcyon.png',
            title: 'Checklist Review',
            artist: 'Ellie Goulding',
            },
            {
            color: '#1F7087',
            src: 'https://cdn.vuetifyjs.com/images/cards/foster.jpg',
            title: 'Submit Request',
            artist: 'Foster the People',
            },
            {
            color: '#952175',
            src: 'https://cdn.vuetifyjs.com/images/cards/halcyon.png',
            title: 'Checklist Review',
            artist: 'Ellie Goulding',
            },
        ],
    }),
    asyncComputed: {
        stage_list: {
            async get() {
                try {
                    const res = await this.$http.get(`http://127.0.0.1:8000/escBackend/stage_kind/`)
                    this.stage_cnt = res.data.length
                    return res.data
                }catch(e) {
                    window.console.log(e)
                }
            }
        },
    },
    computed: {
        process_title: function() {
            return (this.process_object.Kind == 1) ? 'SEE Escalation' : 'EE Escalation'
        },
        process_tryTimes: function() {
            let tryTimesArray = []
            tryTimesArray.push(this.process_object.Stage1TryTimes)
            tryTimesArray.push(this.process_object.Stage2TryTimes)
            tryTimesArray.push(this.process_object.Stage3TryTimes)
            tryTimesArray.push(this.process_object.Stage4TryTimes)
            return tryTimesArray
        }
    },
    methods: {
        
    }

}
</script>