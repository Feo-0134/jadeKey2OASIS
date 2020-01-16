<template>
    <v-container>
        {{process_object}}
        <!-- <Process :process_object= "process_object" /> -->
        <v-timeline dense>
            <v-timeline-item
            v-for="n in items"
            :key="n"
            color="red lighten-2"
            large
            >
            <template v-slot:opposite>
                <span>Tus eu perfecto</span>
            </template>
            <v-card class="elevation-2">
                <v-card-title class="headline">{{n.title}}</v-card-title>
                <v-row>
                <v-card
                    class="mx-10"
                    tile >
                    <v-app-bar
                    dark
                    color="#E57373"
                    >
                    <v-app-bar-nav-icon></v-app-bar-nav-icon>

                    <v-toolbar-title>Stage Context</v-toolbar-title>

                    <v-spacer></v-spacer>

                    <v-btn icon>
                        <v-icon>mdi-magnify</v-icon>
                    </v-btn>
                    </v-app-bar>

                    <v-container>
                    <v-row dense>
                        <v-col cols="12">
                        <v-card
                            color="#385F73"
                            dark
                        >
                            <v-card-title class="headline">Unlimited music now</v-card-title>

                            <v-card-subtitle>Listen to your favorite artists and albums whenever and wherever, online and offline.</v-card-subtitle>
                            <v-file-input class="mx-5" multiple label="File input"></v-file-input>
                            <v-card-actions>
                            <v-btn text>Submit</v-btn>
                            </v-card-actions>
                        </v-card>
                        </v-col>

                        <v-col
                        v-for="(item, i) in itemt"
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
                                v-text="item.title"
                                ></v-card-title>

                                <v-card-subtitle v-text="item.artist"></v-card-subtitle>
                            </div>

                            <v-avatar
                                class="ma-3"
                                size="125"
                                tile
                            >
                                <v-img :src="item.src"></v-img>
                            </v-avatar>
                            </div>
                        </v-card>
                        </v-col>
                    </v-row>
                    </v-container>
                </v-card>
                <v-col>
                <Comment v-for="m in comment_list" :key="m" :comment_object="m" v-show="m.Stage === n.stage"/>
                </v-col>
                </v-row>
                <v-row
                        align="center"
                        justify="start"
                        >
                    <v-btn class="ml-10 mt-5" color="#E57373">
                        new comment
                    </v-btn>
                    <v-spacer></v-spacer>
                    <v-btn class="mr-3" color="primary">
                        Stage pass
                    </v-btn>
                    <v-btn class="mr-10" color="primary">
                        Stage fail
                    </v-btn>
                </v-row>
                <v-card-text>
                    Lorem ipsum dolor sit amet, no nam oblique veritus. Commune scaevola imperdiet nec ut, sed euismod convenire principes at. Est et nobis iisque percipit, an vim zril disputando voluptatibus, vix an salutandi sententiae.
                </v-card-text>
            </v-card>
            </v-timeline-item>
        </v-timeline>
    </v-container>
</template>
<script>
import Comment from '@/components/Comment'
export default {
    props: { },
    components: { Comment },
    data: () => ({
        items: [
            {   
            stage: 1,
            color: '#5F6062',
            src: 'https://cdn.vuetifyjs.com/images/cards/foster.jpg',
            title: 'Submit Request',
            artist: 'Foster the People',
            },
            {
            stage: 2,
            color: '#8E8989',
            src: 'https://cdn.vuetifyjs.com/images/cards/halcyon.png',
            title: 'Checklist Review',
            artist: 'Ellie Goulding',
            },
            {
            stage: 3,
            color: '#5F6062',
            src: 'https://cdn.vuetifyjs.com/images/cards/foster.jpg',
            title: 'Submit Request',
            artist: 'Foster the People',
            },
            {
            stage: 4,
            color: '#8E8989',
            src: 'https://cdn.vuetifyjs.com/images/cards/halcyon.png',
            title: 'Checklist Review',
            artist: 'Ellie Goulding',
            },
            {
            stage: 5,
            color: '#5F6062',
            src: 'https://cdn.vuetifyjs.com/images/cards/foster.jpg',
            title: 'Review Complete',
            artist: 'Foster the People',
            },
        ],
    }),
    asyncComputed: {
        process_object: {
            async get() {
                try {
                    const res = await this.$http.get(`http://127.0.0.1:8000/escBackend/process/${this.process_id}`)
                    return res.data
                }catch(e) {
                    window.console.log(e)
                }
            }
        },
        comment_list: {
            async get(){
                try {
                    let that = this
                    let commentArray = []
                    window.console.log(this.process_object.ProcessComments)
                    for (let n=0;n<this.process_object.ProcessComments.length;n++) {
                        const res = await this.$http.get(`http://127.0.0.1:8000/escBackend/comment/${that.process_object.ProcessComments[n]}`)
                        commentArray.push(res.data)
                    }
                    window.console.log(commentArray)
                    return commentArray
                }catch(e) {
                    window.console.log(e)
                }
            }
        }
    },
    computed: {
        process_id: function() {
            let current_id = this.$router.currentRoute.path.split("/")[2]
            // window.console.log(current_id)
            return current_id
        }
    },
    methods: {
        
    }

}
</script>