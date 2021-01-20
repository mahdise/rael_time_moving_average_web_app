import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from "@angular/common/http";
@Injectable({
  providedIn: 'root'
})
export class PullcrossoverService {
  _url = location.protocol + "//" + location.hostname + ":8000/crossover";
  constructor(private _http: HttpClient) { }

  getStart() {
    //let headers = new HttpHeaders().set('Content-Type', 'text/plain; charset=utf-8');
    let jobj = {
      "user_name" : "mahdi",
      "symbol" : ["AMD","AAPL"],
      "periods" : ["4","10"],
      "result" :"start_info"
      }
    return this._http.post<any>(
      this._url + `/start/`,
      jobj,
      { responseType: "text" as "json" }
    );
  }

  
}
