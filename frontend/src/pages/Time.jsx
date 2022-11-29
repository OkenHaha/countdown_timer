import React from 'react'
import { useState, useEffect } from 'react'
import axios from 'axios'
const api = "http://127.0.0.1/timerapi/"

// function start() {
// 	const [time, setTime] = useState(null)

// 	useEffect(() => {
// 		axios.get("http://127.0.0.1:8000/timerapi/")
// 		.then((response) =>{
// 			setTime(response.data)
// 		})
// 		.catch(err => {
// 			console.table(err)
// 		})
// 	}, [])
// }


const Time = () => {
const [time, setTime] = useState(null)

	const get_date = () => { 
		axios.get("http://127.0.0.1:8000/timerapi/")
		.then((response) =>{
			setTime(response.data)
		})
		.catch(err => {
			console.table(err)
		})
	}
	useEffect(() => {
		const interval = setInterval(get_date, 1000)
		return () => clearInterval(interval)
	}, [])

 const endTime = new Date() + 3000;
 const d = new Date()
 
	return (
		<div>
			{time?.map((time, index) => 
				<div key={index}>
				{time.name} - | - {time.start_time} - | - {time.end_time} - | - {endTime}
				<br/>
				{Math.floor(new Date(time.start_time))} - | - {Math.floor(new Date(time.end_time))}<br/>
				{Math.floor(new Date(time.end_time) - new Date(time.start_time))}<br/>
				{Math.floor(new Date(time.end_time) - new Date(time.start_time))/1000}<br/>
				
				{Math.floor(new Date(endTime))}<br/>
				{d.getTime()}<br/>
				{Math.floor(new Date(time.end_time) - d.getTime())}<br/>
				{d.toLocaleString()}<br/>
				{d.toTimeString()}<br/>
				{new Date(time.start_time).getTime()}
				</div>
			)}
			<h1>Hello</h1>
		</div>
	)
}

export default Time