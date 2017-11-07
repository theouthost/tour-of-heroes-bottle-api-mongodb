import { Injectable }    from '@angular/core';
import { Headers, Http } from '@angular/http';
import 'rxjs/add/operator/toPromise';

import { Hero } from './hero';

@Injectable()
export class HeroService {

private heroesUrl = 'http://127.0.0.1:8080';  // URL to web api

constructor(private http: Http) { }

//Create
create(name: string): Promise<Hero> {
   const url = `${this.heroesUrl}/add`;

  return this.http
    .post(url, JSON.stringify({name: name}), {headers: this.headers})
    .toPromise()
    .then(res => res.json().data as Hero)
    .catch(this.handleError);
}








//Read one Read All

getHeroes(): Promise<Hero[]> {
  return this.http.get(`${this.heroesUrl}/allheroes`)
             .toPromise()
             .then(response => response.json().data as Hero[])
             .catch(this.handleError);
}



  getHero(id: number): Promise<Hero> {
  return this.getHeroes()
             .then(heroes => heroes.find(hero => hero.id === id));
}





private headers = new Headers({'Content-Type': 'application/json'});



//UPDATE

update(hero: Hero): Promise<Hero> {
  const url = `${this.heroesUrl}/update/${hero.id}`;
  return this.http
    .put(url, JSON.stringify(hero), {headers: this.headers})
    .toPromise()
    .then(() => hero)
    .catch(this.handleError);
}



//DELETE
delete(id: number): Promise<void> {
  const url = `${this.heroesUrl}/delete/${id}`;
  return this.http.delete(url, {headers: this.headers})
    .toPromise()
    .then(() => null)
    .catch(this.handleError);
}







//Handle Errors
private handleError(error: any): Promise<any> {
  console.error('An error occurred', error); // for demo purposes only
  return Promise.reject(error.message || error);
}

}
