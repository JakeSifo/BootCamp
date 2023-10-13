package com.webage.store;
import static spark.Spark.get;
import static spark.Spark.post;
import static spark.SparkBase.staticFileLocation;


import java.io.StringReader;
import java.util.ArrayList;

import java.util.HashMap;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;

/**
 * Hello world!
 *
 */
public class App 
{
	static ArrayList<Product> catalog;
	
	static {
		catalog = new ArrayList<Product>();
		
		catalog.add(new Product("1001", "Hawaiian Fashion Sneaker", "Hawaiian-print shoe featuring wraparound racing stripe, padded collar, and gored insets at entry", 64.95, "$64.95", "shoe.jpg"));
		catalog.add(new Product("1002", "Calvin Klein Men's Wilson 2", "Keep it trendy with the rounded toe silhouette. Detailed stitching and paneling amp up the style.", 69.99, "$69.99", "boot.jpg"));
		catalog.add(new Product("1003", "Ray-Ban Men's Aviator Large Metal Polarized Aviator Sunglasses", "Ray-Ban is the world's most iconic eyewear brand and is a global leader in its sector. Every model in the Ray-Ban collection is the product of meticulous, original styling that translates the best of the latest fashion trends into an ever-contemporary look for millions of Ray-Ban wearers around the world.", 119.09, "$119.09", "sunglass.jpg"));
	}
	
    public static void main( String[] args )
    {
    	Gson gson = new GsonBuilder().setPrettyPrinting().create();
    	
    	staticFileLocation("/static");
    	
    	get("/api/v1/product", (req, res) -> {
    		res.type("application/json");
    		
    		return catalog;
    	}, gson::toJson);
    	
    	get("/api/v1/product/:id", "application/json", (req, res) -> {
    		res.type("application/json");
    		
    		String id = req.params("id");
    		
    		for (Product p : catalog) {
    			if (p.getId().equals(id)) {
    				return p;
    			}
    		}
    		
    		res.status(404);
    		
    		return "";
    	}, gson::toJson);
    	
    	post("/api/v1/payment", (req, res) -> {
    		res.type("application/json");
    		
    		Payment p = gson.fromJson(new StringReader(req.body()), Payment.class);
    		HashMap<String, String> result = new HashMap<String, String>();
    		
    		if (p.getCardNumber().endsWith("2")) {
    			result.put("status", "Card was declined.");
    		} else if (p.getCardNumber().endsWith("3")) {
    			result.put("status", "Card has expired.");
    		} else {
    			result.put("status", "OK");
    		}
    		
    		return result;
    	}, gson::toJson);

    }
}
